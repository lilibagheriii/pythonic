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
