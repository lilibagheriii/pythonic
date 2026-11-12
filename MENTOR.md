# Mentor guide

The student drives. Your job is to review, unblock, and sign off at milestones, not to do the work.

## Getting up to date

```bash
git clone git@github.com:lilibagheriii/pythonic.git && cd pythonic
bin/sync                 # later, to get the latest (and push any feedback you wrote)
bin/learn status         # where they are, exercise counts, open parked items and questions
bin/learn questions      # everything waiting on you
bin/learn parked         # everything they've set aside
```

`bin/learn status` reads the logs, so it shows the student's real progress without you opening every file.

## Changing the log format

A chapter's `LOG.md` is created from `templates/LOG.md` when the student first starts that chapter. Edit the template whenever the format should change, for example to add a section or reword the prompts. Every chapter started after that gets the new format, and logs that already exist stay as they are. For a separate project format, add `templates/LOG.project.md`. The scripts only rely on the `**Status:**` line and the `## ` section headings. If a section is missing, the commands add it when they need it. To change what a new exercise file looks like, edit `templates/exercise.py`.

## Adding a lab

A lab is a real-world walkthrough you write for a phase, such as analysing a Kaggle dataset or calling a live API. Labs are optional: they show up in `bin/learn status` and `bin/learn labs`, but `bin/learn next` never moves the student into one.

1. **Make a folder anywhere on disk.** Its `README.md` is the walkthrough: the problem, then the steps and questions. Every other file in it (data, skeleton code, subfolders) is a starter file and goes into the lab's `starter/` folder. A folder that already has a `starter/` keeps it as is. If there's no `README.md`, a stub is created for you.
2. **Add it:**
   ```bash
   bin/learn lab add ~/Desktop/titanic-survivors --needs pcc-04
   ```
   This creates `phase-0-foundations/labs/titanic-survivors/` (the walkthrough plus `starter/`) and lists it as `lab-titanic-survivors` in that phase's `labs` in `curriculum.json`. Junk such as `.git`, `__pycache__` and `.DS_Store` is left out. Options:
   - `--phase N`: which phase. The default is the student's current phase, taken from `.current-chapter`.
   - `--needs <chapter>`: the chapter it builds on. The lab shows as "after pcc-04" until that chapter is done, and completing the chapter tells the student the lab is ready.
   - `--title`: defaults to the README's first `# ` heading.
   - `--goal "..."`: a goal for the lab's checklist. Repeat it for more than one.
   - `--id`: defaults to `lab-<folder name>`.
3. **Run `bin/sync`.**

The student starts it with `bin/learn session lab-titanic-survivors`. This adds a `LOG.md` from `templates/LOG.lab.md` to the lab's folder, next to your walkthrough, and copies `starter/` into a new `exercises/` folder there. When they're done, `bin/learn next` closes the lab and takes them back to the chapter they were on.

**Managing labs.** Every `lab` command takes a full id or a unique part of one (`titanic` finds `lab-titanic-survivors`), and `bin/learn lab <command> -h` explains its options.

| Command | What it does |
|---|---|
| `bin/learn lab list` | Every lab with its folder, starter files, needs, goals and the student's progress (status, exercises, open questions) |
| `bin/learn lab edit <id> --title "..." --needs pcc-06 --goal "..."` | Change details without copying files. `--no-needs` and `--no-goals` clear them. `--phase N` moves the lab and its folder to another phase, but only before the student starts it. |
| `bin/learn lab add <folder> --update` | Copy in a newer version of your original folder. It overwrites files but doesn't delete any, so remove dropped files from the lab's folder yourself. |
| `bin/learn lab remove <id>` | Take it out of `curriculum.json` and delete its folder. If the student has started it, add `--force`: only your `README.md` and `starter/` are deleted, and their `LOG.md` and `exercises/` stay. |

You can also edit a lab's `README.md` and `starter/` directly. Changes reach students who start the lab afterwards. A student who has already started it keeps their copy, and their log keeps the title and goals it started with.

**Answer keys don't go in the repo**, because the student can read everything in it.

## Where to give feedback

- **Phase 0:** the student commits straight to `main`. Write feedback in the **Mentor feedback** section of the chapter's `LOG.md`, then run `bin/sync "Mentor feedback on pcc-04"`. The student gets it on their next `bin/sync`. Logs merge automatically even if you both edited the same one, so keep feedback in `LOG.md` and leave their code files alone. Suggest code changes in the log or in a pull request instead.
- **Answering questions:** reply under the question in **Questions for mentor** (an indented `- ` line), or tell them in person. The student closes it with `bin/learn answered <n> "<summary in their own words>"`. Having them write the summary themselves is the point.
- **Phase 1 onwards:** the student works on a branch per chapter or feature (`git switch -c pcc-18`), and `bin/sync` pushes that branch. They open a pull request, and you review it like a teammate's. Merging is the sign-off.

## Rhythm

| When | What |
|---|---|
| Sprint week (Nov 10–14) | Each evening: a 15-minute look at the day's session entry and any questions. Saturday: the mini-project demo (1h), then help with the retro and Phase 1 plan. |
| Weekly afterwards | A 30-minute check-in. They lead: show `bin/learn status`, demo something, bring parked items and questions. |
| Within 48 hours | Review any pull request they open |
| Each milestone (every `proj-*`) | A demo. Sign off, or send it back with specific gaps. |
| Monthly | They score themselves against the mid-level checklist in PLAN.md, and you check their scores |

## Ground rules

- **The 30-minute rule:** they try for 30 minutes before asking, and their question says what they tried. If it doesn't, ask "what have you tried?" before answering.
- **Ask before you tell:** answer with a question first ("what does the traceback say?"), and give the answer only if they're still stuck.
- **Don't take the keyboard.** Point to the line; they type.
- **Parking is fine.** Moving on and coming back is a skill. Check that `bin/learn parked` shrinks over time and doesn't only grow.
