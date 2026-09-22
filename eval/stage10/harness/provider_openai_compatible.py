#!/usr/bin/env python3
"""Minimal OpenAI-compatible chat-completions provider adapter.

Configuration via constructor (env-bridged in runner.load_provider()).
Supports SYSTEM messages and function/tool calling; stateless per call
(every request carries the full fresh message array; no conversation IDs).
"""
import json
import urllib.request
import urllib.error


class OpenAICompatibleProvider:
    def __init__(self, base_url: str, api_key: str, model: str,
                 extra_headers: dict | None = None, timeout: int = 300):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.model = model
        self.extra_headers = extra_headers or {}
        self.timeout = timeout

    def chat(self, messages, tools=None, temperature=None) -> dict:
        body = {"model": self.model, "messages": messages}
        if tools:
            body["tools"] = tools
            body["tool_choice"] = "auto"
        if temperature is not None:
            body["temperature"] = temperature
        data = json.dumps(body).encode("utf-8")
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer " + self.api_key}
        headers.update({k: v for k, v in self.extra_headers.items()
                        if k.lower() not in ("authorization", "api-key")})
        req = urllib.request.Request(self.base_url + "/chat/completions",
                                     data=data, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:400]
            raise RuntimeError(f"provider HTTP {e.code}: {detail}") from e

    # --- introspection for preflight (no secrets) ---
    def describe(self) -> dict:
        from urllib.parse import urlparse
        host = urlparse(self.base_url).netloc
        return {"provider_class": "openai-chat-compatible", "api_host": host,
                "model": self.model, "secret_source": "runtime env/registry (never committed)"}
