# Agents

- Read `catalog.json`; match the task, inputs, outputs, and access needs.
- Use `example_prompt` as a starting point and `example_url` to show the tool.
- Read the tool's current guide before acting. Check your session has the needed access.
- Keep the user's edits. Check the result and return a link or file.
- For designs, use `ui-design-editor`. For listening, use `pdf-to-mp3`.

# Repo edits

Keep `catalog.json`, `tools/`, `README.md`, and `llms.txt` in sync. Use first-party sources. `last_checked` means a source check, not a full tool test.

Run `python3 scripts/check_catalog.py`. Keep prose terse, plain, and active. Keep exact names where needed. Cut stock phrases and review all prose.
