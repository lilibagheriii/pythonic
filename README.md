# Python Learning Path

My path from first line of code to mid-level Python developer. Each chapter I start gets its own folder with a `LOG.md`, where I keep my exercises, session notes, remarks, questions for my mentor, and anything I've parked to finish later.

**I drive. My mentor reviews, unblocks and signs off.** See [PLAN.md](PLAN.md) for the whole path, [MENTOR.md](MENTOR.md) for how my mentor works with this repo, and [career-roadmap.html](career-roadmap.html) for which jobs this path leads to and roughly when. [intro.html](intro.html) is a one-page version of this README to keep open in a browser.

Two shortcuts do all the bookkeeping:

- **`l`** (learn) keeps the chapter logs.
- **`s`** (sync) saves my work and swaps updates with my mentor on GitHub.

## First-time setup

The repo is already cloned and connected to GitHub. Do these once, in order.

1. **Install Python 3 and PyCharm.** The free Community edition is enough. `pcc-00` walks through this. The book uses VS Code; we use PyCharm instead.
2. **Open the `pythonic` folder in PyCharm** (File → Open).
3. **Give the project its own virtual environment**, so Python tools install into the project and the terminal picks them up by itself:
   - Settings (**⌘,** on Mac, **Ctrl+Alt+S** on Windows) → **Project: pythonic** → **Python Interpreter** → **Add Interpreter** → **Add Local Interpreter**.
   - Choose **Virtualenv Environment**, then **New**. Set the location to the `.venv` folder inside `pythonic` and the base interpreter to your Python 3. Click OK.
   - Check that Settings → **Tools → Terminal → Activate virtualenv** is ticked.
4. **Open PyCharm's terminal** with **⌥F12** (Mac) or **Alt+F12** (Windows). The prompt should start with `(.venv)`. Then install the tools:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. **Install the shortcuts**, still in that terminal:
   ```bash
   bin/install-aliases          # l = learn, s = sync
   ```
   Then open a **new terminal tab** (**⌘T** on Mac, **Ctrl+Shift+T** on Windows). From now on `l` and `s` work in every PyCharm terminal and in any folder.
   If a letter is already taken on your machine, the script says so. Pick others with `bin/install-aliases --learn j --sync y`. Undo with `bin/install-aliases --remove`, and re-run it if you move the repo.
6. **Check the connection to GitHub.** This should end with "✓ In sync.":
   ```bash
   s
   ```
   If it says you don't have access, ask your mentor to check your access to the repo on GitHub.
7. **Start your first chapter:** `l start pcc-00`

**On Windows:** the scripts need Git Bash. Set Settings → Tools → Terminal → **Shell path** to Git Bash (usually `C:\Program Files\Git\bin\bash.exe`), then open a new terminal tab.

## Working in PyCharm

Keep the code in the editor and the commands in the terminal, and move between them with the keyboard.

| What | Mac | Windows / Linux |
|---|---|---|
| Open the terminal, or jump to it | ⌥F12 | Alt+F12 |
| Back to the editor, terminal stays open | Esc | Esc |
| Hide the terminal and go back to the editor | ⇧Esc | Shift+Esc |
| Reopen the last tool window | F12 | F12 |
| New terminal tab | ⌘T | Ctrl+Shift+T |
| Run the file open in the editor | ⌃⇧R | Ctrl+Shift+F10 |

- **F-keys on a Mac:** if they change the volume or brightness, hold **fn** with them, or turn on "Use F1, F2, etc. keys as standard function keys" in macOS keyboard settings.
- **If Esc doesn't leave the terminal:** check Settings → Tools → Terminal → **Move focus to the Editor with**. It should be Escape.

## The daily loop

Start every session with `l session`.

```bash
l session --hours 2                  # 1. first thing: start today's entry in the log
s                                    # 2. get your mentor's latest feedback

l ex 2-1 "Simple Message"            # 3. new file: exercises/ex_2_1_simple_message.py
#                                       4. write it, run it (⌃⇧R / Ctrl+Shift+F10), fix it
l done 2-1                           # 5. tick it off. Repeat 3–5 for each exercise.

s                                    # 6. last thing: save and share
```

Before step 6, open the chapter's `LOG.md` and fill in today's session entry: Did, Learned, Confusing, Next time. One line each is enough.

**Moving to a new chapter?** Run `l start <id>` before `l session`, so the session is logged in the new chapter.

Type the book's examples out by hand. Copy-pasting skips the part where you learn.

## When something gets in the way

| Situation | Command |
|---|---|
| **Stuck.** Try for 30 minutes first, then ask, and say what you tried. | `l ask "Why does 0.1 + 0.2 print 0.30000000000000004? Tried round()"` |
| **Need to move on.** Park it so it isn't forgotten. | `l park "2-8: redo after reading about string methods"` |
| **Learned something.** Write it down while it's fresh. | `l note "f-strings need the f before the quote"` |

`l questions` and `l parked` list what's open across all chapters. Close items with `l answered <n> "what I learned"` and `l unpark <n>`, using the number from those lists.

## Where you are

Show `l status` at the start of every check-in with your mentor.

```
$ l status 0

Phase 0 · Foundations (sprint: Tue Nov 10 – Sat Nov 14, 8h/day)
   ✓ pcc-00   Setup and Git                     complete     ex 3/3
 ▶ … pcc-01   Getting Started                   in-progress  ex 1/2  parked 1  questions 1
   · pcc-02   Variables and Simple Data Types   not-started
```

▶ marks your current chapter. ✓ complete, … in progress, · not started, – skipped. (Example output.)

## Finishing a chapter

1. Fill in the **Retro** at the bottom of the chapter's `LOG.md`.
2. Run `l complete`. If exercises, parked items or the retro are unfinished, it lists them and stops. Finish them, or agree with your mentor to move on and use `l complete --force`. Parked items stay listed, so nothing gets lost.
3. It tells you the next chapter. Run `l start <id>`.

Phase 1 has three project tracks and you pick two. Mark each chapter of the track you skip, for example `l skip pcc-12 "picked data and web tracks"`.

## Chapter logs

A chapter's folder and `LOG.md` appear the first time you run `l start <id>`. Until then the chapter exists only in `curriculum.json` and `l status`. Each log is created from [templates/LOG.md](templates/LOG.md) as it is at that moment, so your mentor can change the template as you go and every chapter started afterwards gets the new format. A project can have its own template in `templates/LOG.project.md`.

| Section | What goes there | Written by |
|---|---|---|
| `**Status:**` line | Where the chapter stands | `l start`, `l complete`, `l skip` |
| Goals | What you should be able to do at the end | you |
| Exercises | A checklist that links to each exercise file | `l ex`, `l done` |
| Session log | One dated entry per study session | `l session` |
| Remarks | Gotchas, aha moments, links | `l note` |
| Questions for mentor | Open questions, then their answers | `l ask`, `l answered` |
| Parked | Unfinished things to come back to | `l park`, `l unpark` |
| Mentor feedback | Arrives with `s` | your mentor |
| Retro | Your look back before completing | you |

Edit any log by hand too. If a section is missing, the commands add it when they need it.

**Side logs.** Some logs run alongside the books, such as job search and algorithm practice. Add `-c <id>` to use a command on one without switching chapters. The first `ex`, `note`, `ask`, `park` or `session` on it starts it.

```bash
l ex 1 "Two Sum" -c add-algorithms
l note "Applied: junior developer role, via referral" -c add-job-search
```

## Syncing

`s` commits everything, gets your mentor's changes, and pushes yours. Run it at the start and end of every session. `l` never commits anything itself.

If you and your mentor both edited the same `LOG.md`, both sets of lines are kept automatically. If you both changed the same lines of a code file, `s` puts everything back the way it was, names the file, and stops. Nothing is lost. Run `s --keep-mine` to keep your version of those lines, or ask your mentor which one to keep.

## All commands

Commands that change a log use your current chapter unless you add `-c <id>`. Ids work without leading zeros, so `pcc-3` finds `pcc-03`. Every command explains itself: `l -h`, `l ex -h`, `s --help`.

| Command | What it does |
|---|---|
| `l session [--hours N]` | Start today's entry in the session log |
| `l status [phase]` | Every chapter with its progress |
| `l start <id>` | Make a chapter current, creating its log from the template the first time |
| `l ex <id> [title]` | Create an exercise file and add it to the checklist |
| `l done <id>` | Tick off an exercise |
| `l note <text>` | Add a remark |
| `l ask <text>` | Ask your mentor something |
| `l questions` | List every unanswered question |
| `l answered <n> [answer]` | Close a question, with the answer in your own words |
| `l park <text>` | Set something aside to finish later |
| `l parked` | List everything still parked |
| `l unpark <n> [note]` | Mark a parked item done |
| `l complete [id] [--force]` | Finish a chapter, after checking for loose ends |
| `l skip <id> [reason]` | Skip a chapter, such as a project track you didn't pick |
| `s [message]` | Save, get your mentor's changes, share yours |
| `s --keep-mine` | Only after a conflict: keep your version of the clashing lines |
| `bin/install-aliases [--learn x --sync y] [--remove]` | Add or remove the `l` and `s` shortcuts |

## Layout

```
pythonic/
├── README.md  PLAN.md  MENTOR.md
├── intro.html  career-roadmap.html
├── curriculum.json            every phase and chapter, in order
├── bin/                       learn, sync, install-aliases
├── templates/                 LOG.md (new chapter logs) and exercise.py (new exercise files)
└── phase-0-foundations/       appears with your first `l start`
    ├── pcc-00-setup-and-git/
    │   ├── LOG.md
    │   └── exercises/         appears with your first `l ex`
    └── proj-mini-mini-project/
        ├── LOG.md
        ├── src/               appears with your first `l ex`
        └── tests/             make this yourself when you write tests
```
