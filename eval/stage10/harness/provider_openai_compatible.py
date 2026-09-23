"""OpenAI-compatible provider adapter for the Stage 10 reference model.

Frozen reference: OpenCode Zen / deepseek-v4-pro.
No fallback path exists. If the reference is unavailable the caller must fail closed.
"""
from __future__ import annotations

import copy
import http.client
import json
import os
import re
import socket
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request

REQUIRED_BASE_URL = "https://opencode.ai/zen/go/v1"
REQUIRED_MODEL = "deepseek-v4-pro"
REQUIRED_TEMPERATURE = 0
REQUIRED_MAX_TOKENS = 16000
LOCAL_PROXY = "http://127.0.0.1:7897"
MAX_TRANSPORT_ATTEMPTS = 3
TRANSPORT_BACKOFF_SECONDS = (1, 3)
REASONING_FIELDS = frozenset({"reasoning", "reasoning_content", "reasoning_details", "thinking", "analysis"})
TECHNICAL_RESPONSE_KEY = "_stage10_technical"


class _FixedLocalProxyHandler(urllib.request.ProxyHandler):
    """Use the configured proxy even when process NO_PROXY settings match the host."""

    def proxy_open(self, req, proxy, type):
        parsed = urllib.parse.urlsplit(proxy)
        if parsed.scheme not in ("http", "https") or not parsed.netloc or parsed.username or parsed.password:
            raise urllib.error.URLError("invalid fixed proxy configuration")
        original_type = req.type
        proxy_type = parsed.scheme
        req.set_proxy(parsed.netloc, proxy_type)
        if original_type == proxy_type or original_type == "https":
            return None
        return self.parent.open(req, timeout=req.timeout)


class ProviderError(RuntimeError):
    """Raised for any provider transport/identity failure."""

    def __init__(self, message: str, technical_metadata: dict | None = None) -> None:
        super().__init__(message)
        self.technical_metadata = technical_metadata or {}


def _load_key_from_local_config() -> str | None:
    """Best-effort read of the OpenCode/OpenCode-Zen key from the local provider config.

    Returns the key or None; never logs the key value.
    """
    home = os.path.expanduser("~")
    for candidate in (
        os.path.join(home, ".opencodex", "config.json"),
    ):
        try:
            with open(candidate, "r", encoding="utf-8") as fh:
                cfg = json.load(fh)
        except (OSError, ValueError):
            continue
        provider = (cfg.get("providers") or {}).get("opencode-go") or {}
        key = provider.get("apiKey")
        if isinstance(key, str) and key:
            return key
        pool = provider.get("apiKeyPool")
        if isinstance(pool, list) and pool:
            first = pool[0] or {}
            k = first.get("key")
            if isinstance(k, str) and k:
                return k
    return None


def load_api_key() -> str:
    """Load the reference API key at runtime. Env var first, local config second."""
    key = os.environ.get("STAGE10_API_KEY")
    if key and key.strip():
        return key.strip()
    key = _load_key_from_local_config()
    if key and key.strip():
        return key.strip()
    raise ProviderError("STAGE10_API_KEY not set and no local opencode-go key found")


def session_header(run_id: str, case_id: str) -> str:
    """Non-secret routing header: unique per case, stable across rounds of one case."""
    if not re.fullmatch(r"[A-Za-z0-9_.\-]+", run_id or ""):
        raise ProviderError("run_id contains forbidden characters")
    if not re.fullmatch(r"[A-Za-z0-9_.\-]+", case_id or ""):
        raise ProviderError("case_id contains forbidden characters")
    return f"stage10-ref-{run_id}-{case_id}"


def _transport_error(exc: BaseException) -> tuple[bool, str, str]:
    """Classify only the explicitly permitted transient transport failures."""
    inner = exc.reason if isinstance(exc, urllib.error.URLError) else exc
    if isinstance(inner, http.client.RemoteDisconnected):
        return True, inner.__class__.__name__, "remote disconnected"
    if isinstance(inner, (socket.timeout, TimeoutError)):
        return True, inner.__class__.__name__, "transport timeout"
    if isinstance(inner, ssl.SSLEOFError) or (
        isinstance(inner, ssl.SSLError)
        and "EOF" in str(getattr(inner, "reason", inner)).upper()
    ):
        return True, inner.__class__.__name__, "TLS EOF"
    if isinstance(inner, ConnectionRefusedError):
        return True, inner.__class__.__name__, "connection refused"
    if isinstance(inner, ConnectionResetError):
        return True, inner.__class__.__name__, "connection reset"
    if isinstance(inner, ConnectionAbortedError):
        return True, inner.__class__.__name__, "connection aborted"
    return False, inner.__class__.__name__, "non-retryable transport failure"


def _usage_summary(usage) -> dict | None:
    """Keep numeric token accounting only; omit prices and arbitrary provider data."""
    if not isinstance(usage, dict):
        return None
    summary = {}
    for key in ("prompt_tokens", "completion_tokens", "total_tokens", "input_tokens", "output_tokens"):
        value = usage.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            summary[key] = value
    for group in ("prompt_tokens_details", "completion_tokens_details", "input_tokens_details", "output_tokens_details"):
        details = usage.get(group)
        if isinstance(details, dict):
            counts = {
                key: value for key, value in details.items()
                if key.endswith("_tokens") and isinstance(value, (int, float)) and not isinstance(value, bool)
            }
            if counts:
                summary[group] = counts
    return summary or None


def _response_diagnostics(data: dict, http_status: int | None,
                          attempts: int, retry_errors: list[dict]) -> dict:
    choices = data.get("choices") or []
    choice = choices[0] if choices and isinstance(choices[0], dict) else {}
    message = choice.get("message") if isinstance(choice.get("message"), dict) else {}
    content = message.get("content")
    reasoning_keys = [key for key in message if key.lower() in REASONING_FIELDS]
    reasoning_values = [message[key] for key in reasoning_keys if message[key] is not None]
    reasoning_length = sum(
        len(value) if isinstance(value, (str, list, dict)) else 0
        for value in reasoning_values
    )
    return {
        "transport_attempt_count": attempts,
        "transport_retry_count": max(0, attempts - 1),
        "retry_errors": copy.deepcopy(retry_errors),
        "http_status": http_status,
        "observed_model": data.get("model"),
        "finish_reason": choice.get("finish_reason"),
        "content_field_present": "content" in message,
        "content_present": content is not None,
        "content_length": len(content) if isinstance(content, str) else (len(content) if isinstance(content, list) else None),
        "reasoning_present": bool(reasoning_keys),
        "reasoning_length": reasoning_length if reasoning_values else None,
        "usage_summary": _usage_summary(data.get("usage")),
    }


def _remove_reasoning_text(value):
    """Return a response copy without hidden reasoning fields or text."""
    if isinstance(value, dict):
        return {
            key: _remove_reasoning_text(child)
            for key, child in value.items()
            if key.lower() not in REASONING_FIELDS
        }
    if isinstance(value, list):
        return [_remove_reasoning_text(child) for child in value]
    return value


def _failure_metadata(attempts: int, retry_errors: list[dict],
                      http_status: int | None = None, observed_model: str | None = None) -> dict:
    return {
        "transport_attempt_count": attempts,
        "transport_retry_count": max(0, attempts - 1),
        "retry_errors": copy.deepcopy(retry_errors),
        "http_status": http_status,
        "observed_model": observed_model,
        "finish_reason": None,
        "content_field_present": False,
        "content_present": False,
        "content_length": None,
        "reasoning_present": False,
        "reasoning_length": None,
        "usage_summary": None,
    }


class ReferenceProvider:
    """Minimal OpenAI chat-completions adapter for the frozen reference model."""

    def __init__(self, api_key: str | None = None, base_url: str = REQUIRED_BASE_URL,
                 model: str = REQUIRED_MODEL, timeout_s: int = 240) -> None:
        if base_url.rstrip("/") != REQUIRED_BASE_URL:
            raise ProviderError(f"provider host validation failed: {base_url!r} != {REQUIRED_BASE_URL!r}")
        if model != REQUIRED_MODEL:
            raise ProviderError(f"provider model validation failed: {model!r} != {REQUIRED_MODEL!r}")
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout_s = timeout_s
        self._key = api_key or load_api_key()
        self._opener = urllib.request.build_opener(
            _FixedLocalProxyHandler({"http": LOCAL_PROXY, "https": LOCAL_PROXY})
        )
        self._sleep = time.sleep

    def chat(self, messages: list[dict], *, tools: list[dict] | None = None,
             tool_choice: str | None = None, session: str | None = None,
             temperature: int = REQUIRED_TEMPERATURE,
             max_tokens: int = REQUIRED_MAX_TOKENS) -> dict:
        """One chat round. Returns the parsed JSON body.

        Generation settings are validated here so no caller can drift them.
        """
        if temperature != REQUIRED_TEMPERATURE:
            raise ProviderError(f"generation settings validation: temperature must be 0, got {temperature}")
        if max_tokens != REQUIRED_MAX_TOKENS:
            raise ProviderError(f"generation settings validation: max_tokens must be 16000, got {max_tokens}")
        body: dict = {
            "model": self.model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "messages": messages,
        }
        if tools is not None:
            body["tools"] = tools
            body["tool_choice"] = tool_choice or "auto"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "stage10-harness/1.0",
            "Authorization": f"Bearer {self._key}",
        }
        if session is not None:
            if "stage10-ref-" not in session or len(session) > 200:
                raise ProviderError("session header validation failed")
            headers["x-opencode-session"] = session
        body_bytes = json.dumps(body, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        retry_errors: list[dict] = []
        last_status = None
        for attempt in range(1, MAX_TRANSPORT_ATTEMPTS + 1):
            req = urllib.request.Request(
                self.base_url + "/chat/completions",
                data=body_bytes,
                headers=headers,
                method="POST",
            )
            try:
                with self._opener.open(req, timeout=self.timeout_s) as resp:
                    last_status = getattr(resp, "status", None)
                    raw = resp.read().decode("utf-8")
            except urllib.error.HTTPError as exc:
                last_status = exc.code
                retryable = exc.code in (502, 503, 504)
                error = {
                    "attempt": attempt,
                    "error_class": exc.__class__.__name__,
                    "error_message": f"HTTP {exc.code}",
                    "http_status": exc.code,
                }
                if retryable:
                    retry_errors.append(error)
                    if attempt < MAX_TRANSPORT_ATTEMPTS:
                        self._sleep(TRANSPORT_BACKOFF_SECONDS[attempt - 1])
                        continue
                raise ProviderError(
                    f"provider HTTP {exc.code}",
                    _failure_metadata(attempt, retry_errors, last_status),
                ) from None
            except Exception as exc:  # noqa: BLE001 - classify the fixed transport allowlist
                retryable, error_class, error_message = _transport_error(exc)
                error = {
                    "attempt": attempt,
                    "error_class": error_class,
                    "error_message": error_message,
                    "http_status": None,
                }
                if retryable:
                    retry_errors.append(error)
                    if attempt < MAX_TRANSPORT_ATTEMPTS:
                        self._sleep(TRANSPORT_BACKOFF_SECONDS[attempt - 1])
                        continue
                    raise ProviderError(
                        f"provider transport failed after {attempt} attempts: {error_class} ({error_message})",
                        _failure_metadata(attempt, retry_errors),
                    ) from None
                raise ProviderError(
                    f"provider transport failure: {error_class} ({error_message})",
                    _failure_metadata(attempt, retry_errors),
                ) from None

            try:
                data = json.loads(raw)
            except ValueError:
                raise ProviderError(
                    "provider returned unparseable JSON",
                    _failure_metadata(attempt, retry_errors, last_status),
                ) from None
            if not isinstance(data, dict):
                raise ProviderError(
                    "provider returned an invalid response shape",
                    _failure_metadata(attempt, retry_errors, last_status),
                )
            observed = data.get("model")
            if observed is not None and observed != REQUIRED_MODEL:
                raise ProviderError(
                    f"provider model drift: requested {REQUIRED_MODEL!r}, observed {observed!r}",
                    _failure_metadata(attempt, retry_errors, last_status, observed),
                )
            safe_data = _remove_reasoning_text(data)
            safe_data[TECHNICAL_RESPONSE_KEY] = _response_diagnostics(data, last_status, attempt, retry_errors)
            return safe_data

        raise AssertionError("unreachable transport retry loop")

    def fetch_usage(self) -> dict | None:
        """Non-secret usage summary if the endpoint supports it."""
        headers = {"Authorization": f"Bearer {self._key}", "User-Agent": "stage10-harness/1.0"}
        req = urllib.request.Request(self.base_url + "/usage", headers=headers, method="GET")
        try:
            with self._opener.open(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, ValueError, OSError):
            return None
