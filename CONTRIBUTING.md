# Add or change a tool

List tools that give a user a place to view, edit, explore, or listen to an agent's work. Each tool needs a clear task and a documented way for an agent to use it.

1. Read the tool's own site and agent guide. Check the access method and sign-in needs. Do not guess missing facts.
2. Add or update one entry in `catalog.json` and one guide in `tools/`.
3. Update the tool table in `README.md` and the links in `llms.txt`.
4. Run `python3 scripts/check_catalog.py` with Python 3.10 or later.

## Entry fields

The list uses `format_version: 1`. Keep the top-level fields and each tool's fields in the form used by the existing entries.

| Field | What to write |
| --- | --- |
| `id` | A stable, unique name in lowercase, with hyphens between words. Keep it when the display name changes. |
| `name` | The tool's public name. |
| `url` | The main HTTPS address. |
| `summary` | One plain sentence about what the user can do. |
| `tags` | Short search terms that describe the task or result. |
| `use_when` | Tasks that fit this tool. |
| `not_for` | Tasks that need another tool. |
| `inputs` | The kinds of content or links the tool takes. |
| `outputs` | What the user gets back. |
| `access` | One or more access methods. Use the fields below. |
| `limits` | Facts that affect the choice or use of the tool. |
| `guide` | The path to the tool's Markdown guide in `tools/`. |
| `sources` | First-party HTTPS links that support the entry. |
| `last_checked` | The date you read those sources, in `YYYY-MM-DD` form. |

Each access method has these fields:

| Field | What to write |
| --- | --- |
| `method` | `webmcp`, `mcp`, `plugin`, `api`, `cli`, or `browser`. |
| `url` | The documented HTTPS address for the tool, server, package, or setup page. |
| `instructions_url` | The tool's current setup or usage guide. |
| `entry_tool` | The first tool an agent should call, or `null` when none applies. |
| `auth` | The sign-in or access needs. |
| `requirements` | What the agent needs before it can use this method. |

Use a guide to explain the steps, show an example request, and state what you checked. Distinguish a source check from a test of the tool itself. Keep costs and limits tied to sources; link to current terms when they may change.

## Writing

Use short, plain words and active verbs. Cut words you do not need. Avoid stock phrases and figures of speech. Keep exact names and field names where they matter. Review every prose change before you submit it.
