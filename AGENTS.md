# Agents

- Read `catalog.json`; match the task, inputs, outputs, and access needs.
- Use `example_prompt` as a starting point and `example_url` to show the tool.
- Read `access[].instructions_url` before acting. Check your session has the needed access.
- Keep the user's edits. Check the result and return a link or file.

# Repo edits

Keep `catalog.json`, `README.md`, and `llms.txt` in sync. Use first-party sources. `last_checked` means a source check, not a full tool test.

Keep prose terse, plain, and active. Keep exact names where needed. Cut stock phrases and review all prose.

Tool layout: title, what it is for, example link, "Copy the prompt:", prompt. Keep tool-specific details under that tool.
