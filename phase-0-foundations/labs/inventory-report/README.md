# Inventory Restock Report: Commenting Exercise

The file `inventory_report_no_comments.py` is a working Python script with every
comment removed. Your job is to put them back, in your own words.

Run it first and read the output, so you know what the script does:

```bash
python3 inventory_report_no_comments.py
```

The script only uses topics from **Python Crash Course, chapters 1 to 5**:
variables, strings, numbers, lists, tuples, `for` loops, list comprehensions,
slicing and `if` statements.

---

## 1. Kinds of comments in Python

### One-line comment

Starts with `#` and a space. Put it **on its own line, above** the code it explains.

```python
# Warn when the order uses 80% of the budget.
BUDGET_WARNING_RATIO = 0.8
```

### Inline comment

A short note at the end of a line. Leave **two spaces** before the `#`.
Use these sparingly, for quick clarifications only.

```python
TOP_N = 3  # number of items shown in the "most valuable" list
```

### Multi-line comment (block comment)

Python has no special symbol for multi-line comments. You write several
one-line comments in a row, each starting with `#`.

```python
# Each product is a tuple with five values:
#   (name, units_on_hand, reorder_point, restock_level, unit_cost)
# reorder_point: reorder when stock falls to this level or below.
```

### Module docstring

A text in triple quotes (`"""`) on the **very first line of the file**. It
describes what the whole script does. Technically it is a string, not a
comment, but this is the standard place to describe a script.

```python
"""One-line summary of what the script does.

A few more lines with details: what it reads, what it prints,
and who would use it.
"""
```

> Do not use triple-quoted strings as comments in the middle of your code.
> That is a docstring's job at the top of the file. Everywhere else, use `#`.

---

## 2. What makes a good comment

| Do | Don't |
|---|---|
| Explain **why** the code is there | Repeat **what** the code already says |
| Write full sentences that start with a capital letter | Write vague notes like `# stuff` or `# fix` |
| Keep comments up to date when the code changes | Leave old comments that no longer match the code |
| Explain values that aren't obvious (`0.8`, column order) | Comment every single line |

Bad, because it repeats the code:

```python
# set top n to 3
TOP_N = 3
```

Good, because it explains the purpose:

```python
# How many of the highest-value products to show at the end of the report.
TOP_N = 3
```

---

## 3. Your tasks

Work from the top of the file to the bottom. Each task says which kind of
comment to use. Tick each box when you're done.

### Top of the file

- [ ] **Module docstring.** In 2 to 4 lines: what does this script do, and
      who would use it?

### Configuration

- [ ] **Section header** (one-line) above `STORE_NAME`. Name the section.
- [ ] **Inline comment** on `RESTOCK_BUDGET`. Why is the number written
      `1_500.00` and not `1500.00`?
- [ ] **Inline comment** on `BUDGET_WARNING_RATIO`. What does `0.8` mean?
- [ ] **Inline comment** on `TOP_N`.
- [ ] **One-line comment** above `DISCONTINUED`. Why is it a tuple and not a list?

### The raw data

- [ ] **Multi-line comment** above `RAW_INVENTORY`. List the five values in
      each tuple, in order, and explain what `reorder_point` and
      `restock_level` mean.
- [ ] Add one more line: why are some of the names messy (extra spaces, mixed
      capital letters)?

### Cleaning the data

- [ ] **Section header** above `inventory`.
- [ ] **One-line comment**: why clean the names once, here, instead of every
      time we use them?

### Working out the results

- [ ] **Section header** above `order_lines`.
- [ ] **Multi-line comment** at the start of this section. Explain what `_`
      means when it appears in the unpacking.
- [ ] **One-line comment** above `order_lines`. Which products make it into
      this list, and which are left out?
- [ ] **One-line comment** above `out_of_stock`.
- [ ] **One-line comment** above `clearance`.
- [ ] **One-line comment** above the three `sum(...)` lines.
- [ ] **Multi-line comment** above `most_valuable`. Why is the value put
      *first* in each tuple? What does `[:TOP_N]` do?
- [ ] **One-line comment** above `healthy`.

### Printing the report

- [ ] **Section header** above the first `print`.
- [ ] **One-line comment**: what does `:.2f` do inside an f-string?
- [ ] **Inline comment** on `if order_lines:`. Why does this work without
      `len(order_lines) > 0`?
- [ ] **One-line comment** above the budget check. When does each branch
      (`if`, `elif`, `else`) run?
- [ ] **One-line comment** above `if out_of_stock:` and above `if clearance:`.
      Why might these sections not print at all?

---

## 4. Check your work

1. Run the script again. Comments must never change the output:

   ```bash
   python3 inventory_report_no_comments.py
   ```

2. Read only your comments, top to bottom, without the code. Could someone
   who has never seen the script understand what it does?

3. Compare your version with `inventory_report.py`, the fully commented
   original. Your wording can be different; that's fine. Check that you
   explained the same ideas.

---

## 5. Bonus

- Change `RESTOCK_BUDGET` to `900` and run the script. Which branch of the
  budget check runs now? Does any comment need updating?
- Add a new product to `RAW_INVENTORY` with a messy name. Does the cleaning
  step handle it?
