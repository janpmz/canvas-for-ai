# Add a tool

1. Check the tool's own docs and agent access.
2. Copy an entry in `catalog.json`; keep all fields and use a unique, stable `id`.
3. Add the tool and prompt to `README.md`; link the tool in `llms.txt`.

Every tool needs:

- `example_prompt`: a short, complete prompt in a copyable `text` block in the README.
- `example_url`: a direct example or usable editor link; `null` if none exists.
- `sources`: first-party links. `last_checked`: the source-check date (`YYYY-MM-DD`).
- `access`: method, HTTPS address, current instructions, first tool name (or `null`), sign-in needs, and requirements.

Keep text terse. Link to full instructions. State limits that affect use; do not guess features or costs.

Tool layout: title, what it is for, example link, "Copy the prompt:", prompt. Keep tool-specific details under that tool.
