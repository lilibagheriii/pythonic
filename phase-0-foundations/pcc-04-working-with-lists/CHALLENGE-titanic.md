# Challenge: Who survived the Titanic?

Your first piece of real data analysis, using only chapters 3 and 4.

The data is Kaggle's most famous beginner dataset: the passenger list from
[Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data),
891 real passengers. It's already turned into Python lists in
[exercises/titanic_data.py](exercises/titanic_data.py). Open that file and look
around before you start.

Data scientists spend most of their time doing exactly this: loading data,
checking it, summarising it and finding the story in it. You'll answer the same
questions people on Kaggle answer first, with nothing but `len`, `sum`, `min`, `max`,
`sorted`, slices, loops and list comprehensions.

## Setup

```bash
l ex 4-T "Titanic"
```

Put this line at the top of the new file. `import` is chapter 8, so for now just
copy it; it works like `import random` did:

```python
from titanic_data import names, survived, fares, ages
```

## Questions

Print the answer to each one, with a label, for example `print(f"Passengers: {len(names)}")`.

1. **How big is it?** How many passengers are there? How many ages? Why are those
   numbers different? (The top of `titanic_data.py` says.)
2. **Look at it.** Print the first 5 names and the last 3, using slices. Print the
   first 10 values of `survived`. What do the 1s and 0s mean?
3. **How many survived?** How many passengers survived, and what percentage is that?
   Hint: `survived` is only 1s and 0s, so `sum` counts the survivors.
   `round(x * 100, 1)` turns 0.3838 into 38.4.
4. **Who survived?** Add the groups to your import line:
   `survived_first_class, survived_second_class, survived_third_class, survived_women, survived_men, survived_children`.
   Work out the survival rate of each group. Which group did best, and which did
   worst? Write the headline in one sentence with `l note "..."`.
5. **Ages.** Find the youngest passenger, the oldest and the average age. Then find
   the **median**: sort the ages and take the one in the middle (`len(...) // 2` gives
   the middle index). Why is the youngest age a fraction?
6. **Money.** Find the cheapest fare, the most expensive and the average. Print the
   5 highest fares using `sorted` and a slice. How many people paid nothing?
   (Look up the list method `count`.)
7. **Rich and poor.** Add `fares_first_class, fares_third_class` to the import.
   How many times more did first class pay than third class, on average?
8. **Who paid the most?** `fares.index(max(fares))` gives the position of the
   highest fare. Use that position to look up the passenger's name, and whether they
   survived.
9. **In today's money.** £1 in 1912 is worth very roughly £150 today. Use a list
   comprehension to make `fares_today`, then print its first 5 values and its maximum.
10. **Your report.** Finish the file by printing a short report of 5–6 lines: the
    findings someone would care about, in plain words.

## Going further (optional)

- 714 ages is an even number, so there are two middle values. The real median is
  the average of both. Work it out.
- Is the average age or the median age a better summary here? Write why in a note.
- Something you wanted to ask but couldn't yet, such as "how many first-class women
  survived"? Park it with `l park "..."`. You'll answer it with `if` in chapter 5,
  and with one line of pandas in Phase 2.
