# UI Design Editor

[Open the editor](https://uidesigneditor.com/) · [Current agent guide](https://uidesigneditor.com/instructions.txt) · [Source code](https://github.com/janpmz/uidesigneditor)

Use this for a design the user can view and edit with you. It suits page and app mockups, screenshots, and shared design reviews.

The editor takes a design brief, text, pictures, screenshots, or an existing Space or project link. It can return a shared design, an editable HTML file, or a PNG.

## Use it as an agent

1. Read the [current guide](https://uidesigneditor.com/instructions.txt).
2. Open the editor in a browser that offers its WebMCP site tools. For existing work, open the user's full Space or project link, including `#space` and `&project`.
3. Find the site's tools and call `read_design`. Read its usage guide and the current tool fields.
4. For new work, create a named project with `create_design`. Use `edit_design` when the user asks you to change existing work. Keep text, boxes, and buttons as separate items the user can edit.
5. Use the latest `projectId` and `revision` for each change. If the project changes while you work, read it again and keep the user's edits.
6. Check the design with `read_design` and a PNG from `export_design`. Use `export_design` for an editable HTML file when needed.
7. Keep the tab open and visible. Give the user the full project link and any files you made.

For a screenshot, use `import_image` with the image as a base64 data URL. Use `mode: "new"` for a new project or `mode: "add"` for the open design. The site's guide covers moving and erasing picture areas and importing saved editor HTML.

If the browser has no site tools, state that it needs a supported browser with those tools enabled. Check the tool list; do not assume that opening the site gives you agent access.

## What the user should know

The site needs no signup. It saves shared projects on its server. Anyone with a Space or project link can view and edit **all projects in that Space**, so treat the link as access to the work. See the [privacy policy](https://uidesigneditor.com/privacy-policy/).

This is a design editor. Choose another tool when the user needs to build and host a working site.

## Example request

> Make two layouts for this settings screen in UI Design Editor. Keep each part editable so I can change the design with you.

Sources checked on 2026-10-19: the [agent guide](https://uidesigneditor.com/instructions.txt) and [site guide](https://uidesigneditor.com/llms.txt). This check covered the docs, not a full edit and export test.
