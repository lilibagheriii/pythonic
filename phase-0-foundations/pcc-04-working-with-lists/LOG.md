# pcc-04 · Working with Lists

**Book:** Python Crash Course, 3rd ed. (Eric Matthes)
**Reading:** Chapter 4
**Phase:** Phase 0 · Foundations (sprint: Tue Nov 10 – Sat Nov 14, 8h/day)
**Status:** complete
**Started:** 2026-11-11
**Completed:** 2026-11-11

> How to work through this log: see [The daily loop](../../README.md#the-daily-loop) in the main README.

## Goals
<!-- What should I be able to do when this is finished? Rewrite these in your own words if it helps. -->
- [ ] Loop over a list
- [ ] Write a list comprehension without looking it up (first declarative idea!)
- [ ] Slice lists; know the difference between a list and a tuple

## Exercises
<!-- Added by `l ex`. Tick off with `l done <id>`. -->
- [x] 4-1 → [ex_4_1.py](exercises/ex_4_1.py) ✓ 2026-11-11
- [x] 4-10 → [ex_4_10.py](exercises/ex_4_10.py) ✓ 2026-11-11
- [x] 4-13 → [ex_4_13.py](exercises/ex_4_13.py) ✓ 2026-11-11

## Session log
<!-- `l session` adds a dated entry. Fill it in before you stop for the day. -->
_None yet._

## Remarks
<!-- Aha moments, gotchas, useful links. `l note "..."` -->
_None yet._

## Questions for mentor
<!-- Tried for 30 minutes first? Say what you tried. `l ask "..."` -->
- [ ] (2026-11-11) 4-10
- [x] (2026-11-11) what is the difference friend_pizzas = pizzas[:] — answered 2026-11-11
  - **Answer:** = pizzas does shallow copy, pizzas[:] creates a deep copy. the shallow copy does not create a new list it just gives a new name to the same list
friend_pizzas = pizzas

## Parked
<!-- Unfinished things to come back to. `l park "..."`, then `l unpark <n>` when it's done. -->
_None yet._

## Mentor feedback
<!-- Written by the mentor, here or in pull request reviews. -->
- 2026-11-11: When the book exercises are done, try [CHALLENGE-titanic.md](CHALLENGE-titanic.md): real Kaggle data, only lists and loops.

## Retro
<!-- Fill this in before `l complete`. -->
- **What clicked:**
- **Still fuzzy:**
- **How I'd explain the main idea to a beginner:**
