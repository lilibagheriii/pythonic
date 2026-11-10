# Python Learning Path

My path from first line of code to mid-level Python developer. Every chapter of every book has its own folder with a `LOG.md`, where I keep my exercises, session notes, remarks, questions for my mentor, and anything I've parked to finish later.

**I drive. My mentor reviews, unblocks and signs off.** See [PLAN.md](PLAN.md) for the whole path and [MENTOR.md](MENTOR.md) for how my mentor works with this repo.

## First-time setup

1. Install Python 3 and VS Code (Phase 0, `pcc-00`, walks through this).
2. Create an empty **private** repository on GitHub (no README), then connect this folder to it:
   ```bash
   git remote add origin https://github.com/<you>/python-learning-path.git
   bin/sync
   ```
3. Add your mentor as a collaborator on GitHub (Settings → Collaborators).
4. Make a virtual environment for tools like pytest:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   python3 -m pip install -r requirements.txt
   ```

On Windows, run the scripts from **Git Bash**, and use `py bin/learn ...` if `bin/learn` alone doesn't run.

## The daily loop

```bash
bin/learn start pcc-02                       # pick up a chapter (only needed when switching)
bin/learn session --hours 8                  # start today's entry in the log

bin/learn ex 2-1 "Simple Message"            # new file: exercises/ex_2_1_simple_message.py
# ...write the code, run it, fix it...
bin/learn done 2-1                           # tick it off

bin/learn note "f-strings need the f before the quote"
bin/learn ask "Why does 0.1 + 0.2 print 0.30000000000000004? Tried: round()"
bin/learn park "2-8: come back after reading about string methods"

bin/sync                                     # save, pull mentor feedback, push. Run it when you start and when you stop.
```

Before you stop for the day, open the chapter's `LOG.md` and fill in the session entry: what you did, what you learned, what confused you, and what's next.

## Finishing a chapter

1. Fill in the **Retro** section at the bottom of the chapter's `LOG.md`.
2. Run `bin/learn complete`. It refuses if there are unfinished exercises, open parked items or an empty retro, and tells you what's left. Either finish them or, if you've agreed with your mentor to move on, use `bin/learn complete --force`. The parked items stay listed so nothing gets lost.
3. It tells you the next chapter. Run `bin/learn start <id>`.

Phase 1 has three project tracks and you pick two. Mark the one you skip with `bin/learn skip pcc-12 "picked data and web tracks"` (and the same for its other chapters).

## All commands

| Command | What it does |
|---|---|
| `bin/learn status [phase]` | Every chapter with its status, exercises done, parked items and open questions. ▶ marks the current chapter. |
| `bin/learn start <id>` | Make a chapter current and mark it in progress |
| `bin/learn session [--hours N]` | Add a dated entry to the session log for you to fill in |
| `bin/learn ex <id> [title]` | Create an exercise file from the template and list it in the log |
| `bin/learn done <id>` | Tick off an exercise |
| `bin/learn note <text>` | Add a remark |
| `bin/learn ask <text>` | Log a question for your mentor |
| `bin/learn questions` | List every unanswered question, across all chapters |
| `bin/learn answered <n> [answer]` | Close question number *n* (from `questions`), with a short summary of the answer |
| `bin/learn park <text>` | Park something unfinished |
| `bin/learn parked` | List everything still parked, across all chapters |
| `bin/learn unpark <n> [note]` | Mark parked item number *n* done |
| `bin/learn complete [id] [--force]` | Mark a chapter complete |
| `bin/learn skip <id> [reason]` | Mark a chapter skipped |
| `bin/learn init` | Create the folder and `LOG.md` for anything new added to `curriculum.json` |
| `bin/sync [message]` | Commit everything, pull mentor changes, push. If you and your mentor both edited a `LOG.md`, both sets of lines are kept. |
| `bin/sync --keep-mine` | Use this only if `bin/sync` says you both changed the same lines of a code file. Keeps your version of those lines. |

Commands that change a log use your current chapter. Add `-c <id>` to target another one, for example `bin/learn unpark 1 -c pcc-03`. Chapter ids work without leading zeros too: `pcc-3` finds `pcc-03`.

## Layout

```
python-learning-path/
├── README.md  PLAN.md  MENTOR.md
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
