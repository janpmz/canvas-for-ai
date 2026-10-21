# Agents

- Read `catalog.json`.
- Match the task, inputs, outputs, and access needs.
- Use `example_prompt` to draft the prompt.
- Use `example_url` to show the tool.
- Read `access[].instructions_url` before you act.
- Check that your session has the needed access.
- Keep the user's edits.
- Check the result.
- Return a link or file.

# Repo edits

Keep tool facts and prompts the same in `catalog.json`, `README.md`, and `llms.txt`. Use the tool's own sources. Set `last_checked` to the source-check date. This date does not mean that you tested the tool.

Use this order for each tool: title, purpose, example link, "Copy the prompt:", prompt. Keep each tool's details under that tool.

# Writing

Read [ASD-STE100](.agents/skills/asd-ste100/SKILL.md) before you write for this project or its chats.

These rules cover all text you write: docs, prompts, comments, page text, GitHub issues, pull requests, commit messages, and chat replies.

- Use the skill's strict rules for steps, errors, and tool text.
- Use the skill's prose rules for docs, reviews, and chat.
- Give one instruction per sentence.
- Keep each instruction to 20 words or fewer.
- Keep each sentence of other prose to 25 words or fewer.
- Use short, plain words and active verbs.
- Use the same word for the same thing.
- Keep each paragraph to one topic and six sentences or fewer.
- Use lists for three or more steps or conditions.
- Do not use semicolons, figures of speech, stock phrases, or claims of quality without facts.
- Cut words that add no meaning.
- Keep every fact, condition, limit, and degree of doubt.
- Keep names, links, code, quotes, and license text exact.
- Keep a longer phrase when a shorter one would change the meaning.
- Review all prose before you send or save it.

Check prose with the skill's script:

```sh
python3 .agents/skills/asd-ste100/scripts/ste-lint.py AGENTS.md CONTRIBUTING.md README.md llms.txt
```

Check prompts and text in `catalog.json` too. The script checks some rules. You must still check meaning and word choice.
