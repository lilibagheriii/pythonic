# Working with Python String

**Phase:** Phase 0 · Foundations (sprint: Tue Nov 10 – Sat Nov 14, 8h/day)
**Written:** 2026-11-13

<!-- Lecture notes for this phase. The student reads these in file-name order, and the
     # heading above is the title `bin/learn lectures` shows. Delete any section you don't need. -->

## Why this matters
<!-- The real-world problem this solves, in two or three sentences. -->
Strings are everywhere, documents, emails, data files, etc. and we're going to need to **parse** them (means digest into meaningful pieces) from time to time.

Remember to visit https://docs.python.org for Python documentation from time to time, they're the creators of the language and it provides a great reference for learning. 

When you try and grasp a problem on your own the concept sticks with you. You'll be able to use the python reference to see what tools are available and apply divide and conquer strategy to split the problem into manageable pieces for which you have tools to address.

## Key ideas
<!-- The few things to remember. One short paragraph or a bullet each. -->
- str is a built-in python data type
- A **string** (`str`) is a sequence of characters. Strings are **immutable**:
every operation below returns a **new** string and leaves the original as it
was.
- The **PCC** column shows the chapter of Python Crash Course that covers each
operation. A dash means it isn't covered in chapters 1 to 5.

## Creating strings

| Syntax | Example | PCC |
|---|---|---|
| Single or double quotes | `'hello'`, `"hello"` | Ch 2 |
| Quotes inside quotes | `"It's fine"`, `'She said "hi"'` | Ch 2 |
| Multi-line (triple quotes) | `"""line one`<br>`line two"""` | - |
| Escape characters | `"Tab:\tNew line:\n"` | Ch 2 |
| f-string | `f"Hello, {name}!"` | Ch 2 |

## Combining and repeating

| Operation | Example | Result | PCC |
|---|---|---|---|
| Join two strings (`+`) | `"sun" + "flower"` | `'sunflower'` | Ch 2 |
| Repeat (`*`) | `"ha" * 3` | `'hahaha'` | - |
| f-string (preferred) | `f"{first} {last}"` | `'ada lovelace'` | Ch 2 |

## Changing case

| Method | Example | Result | PCC |
|---|---|---|---|
| `.title()` | `"ada lovelace".title()` | `'Ada Lovelace'` | Ch 2 |
| `.upper()` | `"ada".upper()` | `'ADA'` | Ch 2 |
| `.lower()` | `"ADA".lower()` | `'ada'` | Ch 2 |
| `.capitalize()` | `"hello world".capitalize()` | `'Hello world'` | - |
| `.swapcase()` | `"Hello".swapcase()` | `'hELLO'` | - |

## Removing whitespace and text

| Method | Example | Result | PCC |
|---|---|---|---|
| `.strip()` | `"  hi  ".strip()` | `'hi'` | Ch 2 |
| `.lstrip()` / `.rstrip()` | `"  hi  ".rstrip()` | `'  hi'` | Ch 2 |
| `.strip(chars)` | `"hi!?".strip("!?")` | `'hi'` | - |
| `.removeprefix()` | `"https://site.com".removeprefix("https://")` | `'site.com'` | Ch 2 |
| `.removesuffix()` | `"report.txt".removesuffix(".txt")` | `'report'` | Ch 2 |

## Indexing and slicing

Strings work like lists: each character has a position, starting at `0`.

| Operation | Example | Result | PCC |
|---|---|---|---|
| First character | `"python"[0]` | `'p'` | Ch 3* |
| Last character | `"python"[-1]` | `'n'` | Ch 3* |
| Slice | `"python"[0:3]` | `'pyt'` | Ch 4* |
| From position 2 to the end | `"python"[2:]` | `'thon'` | Ch 4* |
| Reverse | `"python"[::-1]` | `'nohtyp'` | - |

\* The book shows this on **lists**. It works the same way on strings.

## Checking and measuring

| Operation | Example | Result | PCC |
|---|---|---|---|
| Length | `len("hello")` | `5` | Ch 3* |
| Contains (`in`) | `"ell" in "hello"` | `True` | Ch 5* |
| Doesn't contain | `"z" not in "hello"` | `True` | Ch 5* |
| Equal (case matters) | `"Audi" == "audi"` | `False` | Ch 5 |
| Equal, ignoring case | `"Audi".lower() == "audi"` | `True` | Ch 5 |
| Starts / ends with | `"report.txt".endswith(".txt")` | `True` | - |
| Count occurrences | `"banana".count("a")` | `3` | - |
| Find position | `"banana".find("n")` | `2` (or `-1` if not found) | - |

## Testing what's inside

| Method | Example | Result | PCC |
|---|---|---|---|
| `.isdigit()` | `"2026".isdigit()` | `True` | - |
| `.isalpha()` | `"abc1".isalpha()` | `False` | - |
| `.isspace()` | `"   ".isspace()` | `True` | - |
| `.isupper()` / `.islower()` | `"ABC".isupper()` | `True` | - |

## Splitting, joining, replacing

| Method | Example | Result | PCC |
|---|---|---|---|
| `.split()` | `"a quick fox".split()` | `['a', 'quick', 'fox']` | Ch 10 |
| `.split(sep)` | `"a,b,c".split(",")` | `['a', 'b', 'c']` | Ch 10 |
| `.join()` | `", ".join(["a", "b", "c"])` | `'a, b, c'` | - |
| `.replace()` | `"I like cats".replace("cats", "dogs")` | `'I like dogs'` | Ch 10 |

## Converting

| Operation | Example | Result | PCC |
|---|---|---|---|
| Number to string | `str(42)` | `'42'` | Ch 2 |
| String to whole number | `int("42")` | `42` | Ch 7 |
| String to decimal number | `float("12.5")` | `12.5` | - |
| String to list of characters | `list("abc")` | `['a', 'b', 'c']` | - |

## Formatting inside f-strings

| Format | Example | Result |
|---|---|---|
| 2 decimal places | `f"{12.5:.2f}"` | `'12.50'` |
| Thousands separator | `f"{1500000:,}"` | `'1,500,000'` |
| Percentage | `f"{0.456:.0%}"` | `'46%'` |
| Pad to a width, left-aligned | `f"{'hi':<6}\|"` | `'hi    \|'` |
| Pad to a width, right-aligned | `f"{'hi':>6}\|"` | `'    hi\|'` |
| Show the expression too (debugging) | `f"{total=}"` | `'total=15'` |

## Example

### Immutability in practice

```python
name = "ada"
name.upper()          # returns 'ADA', but name is still 'ada'
name = name.upper()   # store the result to keep it

name[0] = "A"         # TypeError: 'str' object does not support item assignment
```

## Common beginner mistakes

| Mistake | Problem | Fix |
|---|---|---|
| `name.title()` on its own line | The result is thrown away | `name = name.title()` |
| `"Age: " + 30` | `TypeError`: you can't add a string and an int | `f"Age: {30}"` or `"Age: " + str(30)` |
| `'It's'` | The apostrophe ends the string early | `"It's"` |
| `"Audi" == "audi"` | Comparison is case-sensitive | Compare `.lower()` on both sides |
| `"  hi " == "hi"` | Extra spaces don't match | `.strip()` first |


## Try it
<!-- Short exercises. Answer them with `l ex` in the current chapter, or in a lab. -->
1. 

## Further reading
- 
