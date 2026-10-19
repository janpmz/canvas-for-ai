# Canvas for AI

A list of tools where AI agents can show work that people can use, edit, or listen to.

Before you build a page from scratch, check whether a tool here fits the task. Use an existing editor or player when it gives the user a better way to work with the result.

This list serves both people and agents. Each entry says when to use the tool, what it takes, what it makes, and how an agent can use it.

## Find a tool

| Tool | Use it when the user wants to… | Agent access | Guide |
| --- | --- | --- | --- |
| [UI Design Editor](https://uidesigneditor.com/) | View and edit a design, work on a screenshot, or share a design with an agent. | Browser site tools (WebMCP) | [Use UI Design Editor](tools/ui-design-editor.md) |
| [PDF TO MP3](https://pdftomp3.com/) | Listen to text or a document, read along, or get an MP3. | MCP or PDFTOMP3-Plugin | [Use PDF TO MP3](tools/pdf-to-mp3.md) |

## For agents

Start with [AGENTS.md](AGENTS.md) or [llms.txt](llms.txt). Read [catalog.json](catalog.json) to search by task, input, output, or access method. Each entry links to a short guide and the tool's own current instructions.

1. Match the user's task to an entry's `use_when`, `inputs`, and `outputs`.
2. Check `not_for`, `limits`, and the access requirements.
3. Read the entry's guide and the tool's current instructions.
4. Use the tool, check the result, and give the user a link or file they can open.

If no entry fits, tell the user and choose another way to do the task.

## The list

`catalog.json` holds the shared tool data. The guides add steps and examples. The planned website at **canvasforai.com** can use this same data.

`last_checked` records when we read the linked sources. It does not mean we tested every tool action or that a service will always be up.

To add or change a tool, read [CONTRIBUTING.md](CONTRIBUTING.md). Check the list with Python 3.10 or later:

```sh
python3 scripts/check_catalog.py
```
