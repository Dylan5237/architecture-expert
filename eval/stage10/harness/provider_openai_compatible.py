"""OpenAI-compatible provider adapter for the Stage 10 reference model.

Frozen reference: OpenCode Zen / deepseek-v4-pro.
No fallback path exists. If the reference is unavailable the caller must fail closed.
"""
from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request

REQUIRED_BASE_URL = "https://opencode.ai/zen/go/v1"
REQUIRED_MODEL = "deepseek-v4-pro"
REQUIRED_TEMPERATURE = 0
REQUIRED_MAX_TOKENS = 8000


class ProviderError(RuntimeError):
    """Raised for any provider transport/identity failure."""


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
            raise ProviderError(f"generation settings validation: max_tokens must be 8000, got {max_tokens}")
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
        req = urllib.request.Request(
            self.base_url + "/chat/completions",
            data=json.dumps(body).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout_s) as resp:
                raw = resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:400]
            raise ProviderError(f"provider HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise ProviderError(f"provider transport error: {exc}") from exc
        try:
            data = json.loads(raw)
        except ValueError as exc:
            raise ProviderError("provider returned unparseable JSON") from exc
        observed = data.get("model")
        if observed is not None and observed != REQUIRED_MODEL:
            raise ProviderError(
                f"provider model drift: requested {REQUIRED_MODEL!r}, observed {observed!r}"
            )
        return data

    def fetch_usage(self) -> dict | None:
        """Non-secret usage summary if the endpoint supports it."""
        headers = {"Authorization": f"Bearer {self._key}", "User-Agent": "stage10-harness/1.0"}
        req = urllib.request.Request(self.base_url + "/usage", headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, ValueError, OSError):
            return None
