# Python Learning Path

My path from first line of code to mid-level Python developer. Every chapter of every book has its own folder with a `LOG.md`, where I keep my exercises, session notes, remarks, questions for my mentor, and anything I've parked to finish later.

**New here? Open [intro.html](intro.html) in a browser** for a one-page guide to setup, the daily loop and every command. [career-roadmap.html](career-roadmap.html) shows which jobs this path leads to and roughly when.

**I drive. My mentor reviews, unblocks and signs off.** See [PLAN.md](PLAN.md) for the whole path and [MENTOR.md](MENTOR.md) for how my mentor works with this repo.

## First-time setup

You've already cloned this repo (`pythonic`), and it's already connected to GitHub. Run everything below from inside the `pythonic` folder.

1. Install Python 3 and VS Code (Phase 0, `pcc-00`, walks through this).
2. **Install the shortcuts first**, so every step after this one can use them:
   ```bash
   bin/install-aliases          # l = learn, s = sync
   ```
   Then **open a new terminal**. From now on `l` and `s` work from any folder. If a letter is already taken on your machine, the script says so. Pick others with `bin/install-aliases --learn j --sync y`. Undo with `bin/install-aliases --remove`, and re-run it if you move the repo.
3. Check the connection to GitHub. This should end with "✓ In sync.":
   ```bash
   s
   ```
   If it says you don't have access, ask your mentor to check your access to the repo on GitHub.
4. Make a virtual environment for tools like pytest:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   python3 -m pip install -r requirements.txt
   ```
5. Start your first chapter: `l start pcc-00`

On Windows, run everything from **Git Bash**. If `bin/install-aliases` or `bin/learn` won't run, use `py bin/learn ...` and `bash bin/sync` instead of the shortcuts.

## The daily loop

```bash
l start pcc-02                               # pick up a chapter (only needed when switching)
l session --hours 8                          # start today's entry in the log

l ex 2-1 "Simple Message"                    # new file: exercises/ex_2_1_simple_message.py
# ...write the code, run it, fix it...
l done 2-1                                   # tick it off

l note "f-strings need the f before the quote"
l ask "Why does 0.1 + 0.2 print 0.30000000000000004? Tried: round()"
l park "2-8: come back after reading about string methods"

s                                            # save, pull mentor feedback, push. Run it when you start and when you stop.
```

Before you stop for the day, open the chapter's `LOG.md` and fill in the session entry: what you did, what you learned, what confused you, and what's next.

## Finishing a chapter

1. Fill in the **Retro** section at the bottom of the chapter's `LOG.md`.
2. Run `l complete`. It refuses if there are unfinished exercises, open parked items or an empty retro, and tells you what's left. Either finish them or, if you've agreed with your mentor to move on, use `l complete --force`. The parked items stay listed so nothing gets lost.
3. It tells you the next chapter. Run `l start <id>`.

Phase 1 has three project tracks and you pick two. Mark the one you skip with `l skip pcc-12 "picked data and web tracks"` (and the same for its other chapters).

## All commands

| Command | What it does |
|---|---|
| `l status [phase]` | Every chapter with its status, exercises done, parked items and open questions. ▶ marks the current chapter. |
| `l start <id>` | Make a chapter current and mark it in progress |
| `l session [--hours N]` | Add a dated entry to the session log for you to fill in |
| `l ex <id> [title]` | Create an exercise file from the template and list it in the log |
| `l done <id>` | Tick off an exercise |
| `l note <text>` | Add a remark |
| `l ask <text>` | Log a question for your mentor |
| `l questions` | List every unanswered question, across all chapters |
| `l answered <n> [answer]` | Close question number *n* (from `questions`), with a short summary of the answer |
| `l park <text>` | Park something unfinished |
| `l parked` | List everything still parked, across all chapters |
| `l unpark <n> [note]` | Mark parked item number *n* done |
| `l complete [id] [--force]` | Mark a chapter complete |
| `l skip <id> [reason]` | Mark a chapter skipped |
| `bin/install-aliases [--learn x --sync y] [--remove]` | Add or remove the one-letter shortcuts |
| `l init` | Create the folder and `LOG.md` for anything new added to `curriculum.json` |
| `s [message]` | Commit everything, pull mentor changes, push. If you and your mentor both edited a `LOG.md`, both sets of lines are kept. |
| `s --keep-mine` | Use this only if `s` says you both changed the same lines of a code file. Keeps your version of those lines. |

Commands that change a log use your current chapter. Add `-c <id>` to target another one, for example `l unpark 1 -c pcc-03`. Chapter ids work without leading zeros too: `pcc-3` finds `pcc-03`.

## Layout

```
pythonic/
├── README.md  PLAN.md  MENTOR.md
├── intro.html  career-roadmap.html
├── curriculum.json            every phase and chapter; `bin/learn init` builds folders from it
├── bin/learn  bin/sync         helper scripts
├── templates/                 LOG.md and exercise file templates
├── phase-0-foundations/       Python Crash Course, Part I + mini project
│   ├── pcc-00-setup-and-git/
│   │   ├── LOG.md
│   │   └── exercises/         appears with your first `bin/learn ex`
│   ├── pcc-01-getting-started/
│   ├── ...
│   └── proj-mini-mini-project/
│       ├── LOG.md
│       ├── src/               appears with your first `bin/learn ex`
│       └── tests/             make this yourself when you write tests
├── phase-1-build/             Python Crash Course, Part II + deployed app
├── phase-2-functions/         Composing Programs, CS 61A Hog, SQL + declarative refactor
├── phase-3-fluent/            Fluent Python + capstone
└── phase-4-design/            Architecture Patterns with Python, Pragmatic Programmer + open source
```

You can edit any `LOG.md` by hand too. The scripts only need the `## ` section headings and the `**Status:**` line left as they are.
