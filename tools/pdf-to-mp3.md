# PDF TO MP3

[Open the reader](https://pdftomp3.com/) · [Connect an agent](https://pdftomp3.com/connect-ai/) · [Current tool guide](https://pdftomp3.com/llms.txt)

Use this when the user wants to listen to text or a document. The reader lets them read along, replay a sentence, move at their own pace, and ask about the text. It also offers MP3 files for documents and chapters.

## Connect

Follow the [current setup guide](https://pdftomp3.com/connect-ai/). Use a connection the user already has when you can.

| Method | Setup |
| --- | --- |
| MCP | Add `https://pdftomp3.com/mcp` with Streamable HTTP. Sign in to Document Player and approve the connection. The published connection name is `PDFTOMP3-MCP`. |
| PDFTOMP3-Plugin | Follow the site's install steps for [PDFTOMP3-Plugin](https://github.com/janpmz/pdftomp3-plugin), connect the account, and read the installed setup and reading guides. |

Check the current tool list and fields after you connect. Names may carry an app or server prefix.

## Send text to the reader

For plain text, use `send_to_doc_player`. It takes `text`, plus an optional `title` and `request_id`:

```json
{
  "text": "The text the user wants to hear.",
  "title": "Project notes",
  "request_id": "project-notes-001"
}
```

Reuse the same `request_id` when you retry the same passage. Use a new one for new text.

Return the reader link from the tool. The user opens it and presses Play. Sending text does not open the reader or start playback.

## Prepare a document

Read the PDF or document, then follow the connected tool's document workflow. `send_to_doc_player` takes text, not a PDF file. Follow the user's choice to keep the source wording or explain it in plain words.

Document speech needs a saved OpenAI or Gemini speech key. Check setup with the connected tools and use the site's settings page when the user needs to add a key. Follow the tool's steps to prepare the text, create speech when the user asks for it, and return the reader link or MP3.

## Limits

- Listening to text sent by an agent needs a Document Player account. Speech allowances or charges apply.
- Prepared document speech can incur charges through the user's saved speech key.
- Text sent through `send_to_doc_player` expires after 30 days. Each account can keep 100 passages, each up to 100,000 characters.
- A reader link shows where to listen. It does not prove that playback has started.

## Example request

> Send these notes to PDF TO MP3 so I can listen to them and read along one sentence at a time.

Sources checked on 2026-10-19: the [site guide](https://pdftomp3.com/llms.txt) and [connection guide](https://pdftomp3.com/connect-ai/). This check covered the docs, not a full speech test.
