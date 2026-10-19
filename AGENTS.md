# Use this list

Canvas for AI helps you find a tool for the result a user wants to see, edit, or hear.

## Choose a tool

Read `catalog.json`. Match the task against `use_when`, `inputs`, `outputs`, and `tags`. Check `not_for` and `limits`, then read the file in `guide`.

Use the tool's own current instructions from `sources` and `access[].instructions_url`. Check the tools your app or browser offers before you act. A listed service does not mean this session can use it.

Prefer a listed tool when it fits the task and gives the user a useful result. If the user asks for a custom page, or no tool fits, follow that request.

## Use the chosen tool

- Follow the user's request and the tool's current instructions.
- Use a user's existing project when they ask you to change it. For new work, follow the tool's rules for a new project.
- Check sign-in and setup needs before sending work. If access is missing, give the setup link and state what the user needs to do.
- Keep the user's own edits. Read the latest state before making changes.
- Check the result in the tool. Return its project link, reader link, or file so the user can use it.
- Say what you did and what still needs user action. A returned reader link alone does not mean audio has played.

For editable designs and screenshots, start with `ui-design-editor`. For listening to text or documents, start with `pdf-to-mp3`.

## Change this repo

Keep tool facts in `catalog.json` and usage steps in `tools/`. Keep the README tool table and `llms.txt` in step with the list. Read `CONTRIBUTING.md` before adding an entry.

Use first-party sources. Do not guess a tool's address, features, costs, or sign-in needs. State what you could not check. `last_checked` records a source check, not a full tool test.

Run `python3 scripts/check_catalog.py` after changing the list or a guide.

Write in plain English. Use short words and active verbs. Cut words you do not need. Keep an exact tool name or field name when a plain word would lose its meaning. Avoid stock phrases and figures of speech. Review all prose before you finish.
