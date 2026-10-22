# Add a tool

1. Check the tool's own docs and agent access.
2. Copy an entry in `catalog.json`.
3. Keep all fields.
4. Use a unique `id` that will stay the same.
5. Add the tool and prompt to `README.md`.
6. Add the tool link to `llms.txt`.

Every tool needs:

- `example_prompt`: Give a short, complete prompt in a `text` block that the reader can copy from the README.
- `example_url`: Give a direct example or usable editor link. Use `null` if none exists.
- `sources`: Give links to the tool's own sources.
- `repository_url`: Link to the open source repo. Use `null` if none exists. Link the repo in `README.md` and `llms.txt` too.
- `last_checked`: Give the source-check date (`YYYY-MM-DD`).
- `access`: Give the method, HTTPS address, current instructions, first tool name (or `null`), sign-in needs, and requirements.

Keep text short. Link to full instructions. State limits that affect use. Do not guess features or costs.

Use this order for each tool: title, purpose, example link, "Copy the prompt:", prompt. Keep each tool's details under that tool.

## Writing

Use the [writing rules in AGENTS.md](AGENTS.md#writing) for all project text and chats.

The repo includes the [ASD-STE100 skill](.agents/skills/asd-ste100/SKILL.md) from [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill/tree/cd62d297d5ef7cf9f59718cadc233ab2876ea013).
The copy uses source commit `cd62d297d5ef7cf9f59718cadc233ab2876ea013`.
