# Variables, Types and Assignment Operator

**Phase:** Phase 0 · Foundations (sprint: Tue Nov 10 – Sat Nov 14, 8h/day)
**Written:** 2026-11-12

<!-- Lecture notes for this phase. The student reads these in file-name order, and the
     # heading above is the title `bin/learn lectures` shows. Delete any section you don't need. -->

## Why this matters
<!-- The real-world problem this solves, in two or three sentences. -->

Although the crash course covers a lot of the python language syntax, it doesn't necessarily help us become an insider. As we move along, we'll stop and stare a bit deeper, fiddle with the examples to try and understand what happens behind the scene.

## Key ideas
<!-- The few things to remember. One short paragraph or a bullet each. -->

### Assignment operator

Python is dynamically typed, that means when you define a variable using assignment operator (left-hand side which is the label), the interpreter will determine the type of literal or value being assigned (right-hand side which is where the box in memory is).

1. The variable has no fixed type; the value does. A variable is a name attached to a value, and you can attach the same name to a value of any type. This is called dynamic typing.

2. Python has no real constants. Writing a name in **ALL_CAPS** is only a convention that tells other developers "don't change this". Python doesn't enforce it.

### Built-in Functions vs Methods

The difference is in how you call them and what they belong to.

E.g. `sorted()` is a **built-in function**. `str.title()` is a **method**.

| | Function: `sorted()` | Method: `str.title()` |
|---|---|---|
| **How you call it** | `sorted(names)`, passing the value in | `name.title()`, with a dot after the value |
| **Belongs to** | Nothing in particular; it's always available | One type only (`str` here) |
| **Works on** | Any collection you can loop over: list, tuple, string, range | Only strings |
| **Examples** | `len()`, `sum()`, `min()`, `max()`, `print()`, `sorted()` | `.upper()`, `.strip()`, `.append()`, `.sort()` |


### Python Built-in Types

These sizes were measured on **CPython 3.15, 64-bit macOS** using `sys.getsizeof()`. They are in **bytes** and can differ between Python versions and platforms.

| Category | Type | Example | Size in memory (bytes) | Immutable? |
|---|---|---|---|---|
| **Text** | `str` | `"hammer"` | 41 for an empty string, plus about 1 per ASCII character (`"hammer"` = 47) | ✅ Yes |
| **Numbers** | `int` | `42`, `1_500` | 28 for small values; grows with size (`2**60` = 36) | ✅ Yes |
| | `float` | `12.50` | 24 (always) | ✅ Yes |
| | `complex` | `3 + 2j` | 32 | ✅ Yes |
| **Boolean** | `bool` | `True`, `False` | 28 | ✅ Yes |
| **Sequences** | `list` | `[1, 2, 3]` | 56 empty, plus 8 per item (`[1, 2, 3]` = 88) | ❌ No |
| | `tuple` | `(1, 2, 3)` | 48 empty, plus 8 per item (`(1, 2, 3)` = 72) | ✅ Yes |
| | `range` | `range(10)` | 48 (the same for `range(1_000_000)`) | ✅ Yes |
| **Mapping** | `dict` | `{"name": "hammer"}` | 64 empty; 184 with 1 key | ❌ No |
| **Sets** | `set` | `{1, 2, 3}` | 216 (grows in steps as items are added) | ❌ No |
| | `frozenset` | `frozenset({1, 2, 3})` | 216 | ✅ Yes |
| **Binary** | `bytes` | `b"abc"` | 33 empty, plus 1 per byte (`b"abc"` = 36) | ✅ Yes |
| | `bytearray` | `bytearray(b"abc")` | 64 empty; 100 for `b"abc"` | ❌ No |
| | `memoryview` | `memoryview(b"abc")` | 184 | Depends on the data it views |
| **None** | `NoneType` | `None` | 16 | ✅ Yes |

Check a size yourself

```python
import sys

print(sys.getsizeof(12.50))      # 24
print(sys.getsizeof([1, 2, 3]))  # 88
```

### Immutable Types

When a data type is immutable, the only way to change the value is to throw away the old value and then create a new value in memory. Mutable types on the other hand allow changing value in memory.


```python
name = "hammer"
a = name
name.upper()          # creates "HAMMER"; name is still "hammer"
name = name.upper()   # name now points to the new value
print(a)              # a is unchanged - immutable

items = [1, 2]
b = items
items.append(3)       # the same list changes in place: [1, 2, 3]
print(b)              # b is also changed - mutable

```




When a method or function changes the value in its parameters, it's called mutating.

New value or change the original?

| Call | Kind | Original changed? | Returns |
|---|---|---|---|
| `sorted(items)` | function | No | A new sorted list |
| `items.sort()` | list method | **Yes, in place** | `None` |
| `name.title()` | str method | No (strings can't be changed) | A new string |


## Example
<!-- A small, complete example to type out and run. -->

```python
sorted([3, 1, 2])        # [1, 2, 3]
sorted("cab")            # ['a', 'b', 'c']   (works on many types)

"paint roller".title()   # 'Paint Roller'
[3, 1, 2].title()        # AttributeError: lists have no .title()


items = [3, 1, 2]
new = sorted(items)   # items is still [3, 1, 2]; new is [1, 2, 3]
items.sort()          # items is now [1, 2, 3]

name = "hammer"
name.title()          # returns 'Hammer', but name is still 'hammer'
name = name.title()   # store the result to keep it

```

## Common mistakes

> **Common beginner trap:** `items = items.sort()` sets `items` to `None`,
> because `.sort()` changes the list in place and returns nothing.


## Try it
<!-- Short exercises. Answer them with `l ex` in the current chapter, or in a lab. -->
1. 

## Further reading
- 
