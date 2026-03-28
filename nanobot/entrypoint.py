import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG_SRC = ROOT / "config.json"
CONFIG_OUT = ROOT / "config.resolved.json"
WORKSPACE = ROOT / "workspace"


def env(*names: str, default: str = "") -> str:
    for name in names:
        value = os.environ.get(name)
        if value not in (None, ""):
            return value
    return default


def as_int(value: str, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def main() -> None:
    cfg = json.loads(CONFIG_SRC.read_text())

    # Provider (support both LLM_API_* and NANOBOT_LLM_API_*)
    providers = cfg.setdefault("providers", {})
    custom = providers.setdefault("custom", {})
    llm_base = env("LLM_API_BASE_URL", "NANOBOT_LLM_API_BASE_URL", default=custom.get("baseUrl", "http://qwen-code-api:8080/v1"))
    llm_key = env("LLM_API_KEY", "NANOBOT_LLM_API_KEY", default=custom.get("apiKey", ""))
    llm_model = env("LLM_API_MODEL", "NANOBOT_LLM_API_MODEL", "NANOBOT_LLM_MODEL", default=custom.get("model", "coder-model"))

    custom["baseUrl"] = llm_base
    custom["apiBase"] = llm_base
    custom["apiKey"] = llm_key
    custom["model"] = llm_model

    # Agent defaults
    defaults = cfg.setdefault("agents", {}).setdefault("defaults", {})
    defaults["provider"] = "custom"
    defaults["model"] = llm_model

    # Gateway
    gateway = cfg.setdefault("gateway", {})
    gateway["host"] = env("NANOBOT_GATEWAY_CONTAINER_ADDRESS", default=gateway.get("host", "0.0.0.0"))
    gateway["port"] = as_int(env("NANOBOT_GATEWAY_CONTAINER_PORT", default=str(gateway.get("port", 18790))), 18790)

    # WebChat channel
    channels = cfg.setdefault("channels", {})
    webchat = channels.setdefault("webchat", {})
    webchat["enabled"] = True
    webchat["host"] = env("NANOBOT_WEBCHAT_CONTAINER_ADDRESS", default=webchat.get("host", "0.0.0.0"))
    webchat["port"] = as_int(env("NANOBOT_WEBCHAT_CONTAINER_PORT", default=str(webchat.get("port", 8765))), 8765)
    webchat["allow_from"] = ["*"]

    access_key = env("NANOBOT_ACCESS_KEY", default="")
    if access_key:
        webchat["access_key"] = access_key
        webchat["accessKey"] = access_key

    # MCP LMS
    mcp = cfg.setdefault("tools", {}).setdefault("mcpServers", {})
    lms = mcp.setdefault("lms", {})
    lms["command"] = "python"
    lms["args"] = ["-m", "mcp_lms", env("NANOBOT_LMS_BACKEND_URL", default="http://backend:8000")]
    lms_env = lms.setdefault("env", {})
    lms_env["NANOBOT_LMS_API_KEY"] = env("NANOBOT_LMS_API_KEY", default=lms_env.get("NANOBOT_LMS_API_KEY", ""))

    CONFIG_OUT.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n")

    os.execvp(
        "nanobot",
        [
            "nanobot",
            "gateway",
            "--config",
            str(CONFIG_OUT),
            "--workspace",
            str(WORKSPACE),
        ],
    )


if __name__ == "__main__":
    main()
