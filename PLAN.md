# The plan: beginner to mid-level Python developer

Realistic timeline: **18–24 months.** The sprint week builds the base at 8 hours a day. After that it's part-time, about 6–8 hours a week (three weeknights of about an hour, plus 3–4 hours at the weekend).

Every chapter below has a folder and a `LOG.md`. `bin/learn status` shows where things stand.

## Phase 0 · Foundations (sprint: Tue Nov 10 – Sat Nov 14, 8h/day)
**Book:** *Python Crash Course*, 3rd ed., Part I

| Day | Logs | Done when |
|---|---|---|
| Tue | `pcc-00` (Appendices A, B, D), `pcc-01`, `pcc-02`, `pcc-03` | Repo live on GitHub, Ch 1–3 exercises pushed |
| Wed | `pcc-04`, `pcc-05`, `pcc-06` | Can write a list comprehension without looking it up |
| Thu | `pcc-07`, `pcc-08` | Can explain return values vs side effects |
| Fri | `pcc-09`, `pcc-10`, `pcc-11` | Has a pytest suite that passes |
| Sat | `proj-mini`: build (~6h), demo to mentor (1h), retro and Phase 1 plan (1h) | Mentor signs off |

A sprint day: 2h reading and typing the examples, 2h exercises, 1h break, 2h next chapter, 1h review + `bin/learn session` + `bin/sync`.
If Friday runs long, move `pcc-11` to Saturday morning and give the mini project 4 hours.

## Phase 1 · Build real things (weeks 2–7)
*Python Crash Course*, Part II. Pick two of three tracks, and `bin/learn skip` the third.
- Game: `pcc-12` – `pcc-14`
- **Data** (recommended): `pcc-15` – `pcc-17`
- **Web** (recommended): `pcc-18` – `pcc-20`

**Milestone `proj-deployed-app`:** a web app live at a public URL, with a README write-up.

## Phase 2 · Think in functions and declarative style (weeks 8–17)
*Composing Programs* with CS 61A labs and homework.
- `cp-1.1` – `cp-1.5`, then `cp-1.6` Higher-Order Functions and `cp-1.7` Recursive Functions
- `cs61a-hog`: the CS 61A Hog project
- `cp-2.1` – `cp-2.5`, `cp-2.8` Efficiency, `cp-2.9` Recursive Objects
- `cp-4.2` Implicit Sequences, `cp-4.3` Declarative Programming, `sqlbolt`

**Milestone `proj-declarative-refactor`:** rewrite a Phase 1 project in declarative style and explain the difference.

## Phase 3 · Write Python like an experienced developer (months 5–9)
*Fluent Python*, 2nd ed.: `fp-01`, `fp-02`, `fp-03`, `fp-05`, `fp-07`, `fp-08`, `fp-09`, `fp-10`, `fp-13`, `fp-17`, `fp-18`.

**Milestone `proj-capstone`:** a project with a real user, using mypy, ruff, pytest, GitHub Actions and a database.

## Phase 4 · Design and teamwork (months 9–18)
- *Architecture Patterns with Python*: `ap-01` – `ap-06`
- *The Pragmatic Programmer*: `pragprog`, one topic a week
- **Milestone `proj-oss`:** 3 merged open-source pull requests, and reviews of at least 5 pull requests

## Mid-level checklist
Score yourself monthly. Your mentor checks the scores.
- [ ] Takes a vague ticket all the way to a merged pull request without step-by-step help
- [ ] Writes tests first or alongside the code, without being asked
- [ ] Debugs with a debugger and logs, not only `print`
- [ ] Reads an unfamiliar codebase and makes a safe change in it
- [ ] Writes SQL joins and aggregations, and understands indexes at a basic level
- [ ] Understands HTTP and REST, and has built and deployed an API
- [ ] Uses Git branches, rebases, and resolves merge conflicts
- [ ] Gives useful code review and takes feedback without getting defensive
- [ ] Chooses between functional, object-oriented and declarative styles on purpose and can explain why
