"""Check the tool list without extra packages."""

import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
TOOL_FIELDS = {
    "id", "name", "url", "summary", "tags", "use_when", "not_for", "inputs",
    "outputs", "access", "limits", "sources", "last_checked",
    "example_prompt", "example_url",
}
ACCESS_FIELDS = {
    "method", "url", "instructions_url", "entry_tool", "auth", "requirements",
}
METHODS = {"webmcp", "mcp", "plugin", "api", "cli", "browser"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}: needs text")


def text_list(value, label):
    require(isinstance(value, list) and bool(value), f"{label}: needs a nonempty list")
    for item in value:
        text(item, label)
    require(len(value) == len(set(value)), f"{label}: contains repeated values")


def https_url(value, label):
    text(value, label)
    parsed = urlsplit(value)
    require(
        parsed.scheme == "https" and bool(parsed.hostname)
        and parsed.username is None and parsed.password is None
        and not any(char.isspace() for char in value),
        f"{label}: needs an HTTPS URL without sign-in details",
    )


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Repeated JSON key: {key}")
        result[key] = value
    return result


def check():
    catalog = json.loads(
        (ROOT / "catalog.json").read_text(encoding="utf-8"),
        object_pairs_hook=unique_keys,
    )
    require(isinstance(catalog, dict), "The catalog must be an object")
    require(
        set(catalog) == {"format_version", "name", "description", "repository_url", "tools"},
        "Unexpected or missing catalog fields",
    )
    require(type(catalog["format_version"]) is int and catalog["format_version"] == 1,
            "Unsupported format_version")
    for field in ("name", "description"):
        text(catalog[field], field)
    https_url(catalog["repository_url"], "repository_url")
    require(isinstance(catalog["tools"], list) and catalog["tools"], "No tools listed")

    seen = set()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    for tool in catalog["tools"]:
        require(isinstance(tool, dict) and set(tool) == TOOL_FIELDS,
                "Unexpected or missing tool fields")
        label = tool["id"]
        text(label, "id")
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", label), f"Invalid id: {label}")
        require(label not in seen, f"Repeated id: {label}")
        seen.add(label)
        for field in ("name", "summary", "last_checked"):
            text(tool[field], f"{label}.{field}")
        https_url(tool["url"], f"{label}.url")
        for field in ("tags", "use_when", "not_for", "inputs", "outputs", "limits", "sources"):
            text_list(tool[field], f"{label}.{field}")
        for source in tool["sources"]:
            https_url(source, f"{label}.sources")
        checked = date.fromisoformat(tool["last_checked"])
        require(checked.isoformat() == tool["last_checked"], f"{label}: use YYYY-MM-DD")

        require(tool["name"] in readme and tool["url"] in llms,
                f"{label}: add the tool to README.md and llms.txt")

        text(tool["example_prompt"], f"{label}.example_prompt")
        prompt_block = f"```text\n{tool['example_prompt']}\n```"
        require(prompt_block in readme,
                f"{label}: add the copyable prompt to README.md")
        if tool["example_url"] is not None:
            https_url(tool["example_url"], f"{label}.example_url")
            require(tool["example_url"] in readme and tool["example_url"] in llms,
                    f"{label}: add the example link to README.md and llms.txt")

        require(isinstance(tool["access"], list) and tool["access"], f"{label}: no access method")
        for access in tool["access"]:
            require(isinstance(access, dict) and set(access) == ACCESS_FIELDS,
                    f"{label}: unexpected or missing access fields")
            require(isinstance(access["method"], str) and access["method"] in METHODS,
                    f"{label}: unknown access method")
            for field in ("url", "instructions_url"):
                https_url(access[field], f"{label}.access.{field}")
            if access["entry_tool"] is not None:
                text(access["entry_tool"], f"{label}.access.entry_tool")
            text(access["auth"], f"{label}.access.auth")
            text_list(access["requirements"], f"{label}.access.requirements")

    print(f"Checked {len(seen)} tools.")


if __name__ == "__main__":
    try:
        check()
    except (ValueError, TypeError, KeyError, OSError) as error:
        raise SystemExit(f"Catalog check failed: {error}") from error
