# Lab: Readability Checker

**Time:** 45 to 60 minutes
**Covers:** Python Crash Course, chapters 1 to 5
**Files:** `starter.py` (your work goes here)

---

## The problem

You work with the content team that writes the **help-centre articles** for an
online shop. Customers who read these articles are often stressed: they're
locked out or an order went wrong. Hard-to-read text means more support calls.

The team lead asks you:

> "Before we publish an article, I want a quick readability check. Tell me
> how many words and sentences it has, how long the sentences and words are,
> and give me a readability score. Point out the long words and the filler
> words we should cut. Then tell me whether it's ready to publish."

The first article to check, "How to reset your password", is already in
`starter.py`.

## The readability score: LIX

**LIX** is a real readability index, created by the Swedish researcher
Carl-Hugo Björnsson in 1968. It's popular because it needs only counting,
with no syllables or dictionaries, and it works across many languages.

```text
LIX = (words / sentences) + (long words x 100 / words)
```

- A **long word** has **7 or more letters**.
- The first part measures **sentence length**. The second is the
  **percentage of long words**.

| LIX score | Reading level |
|---|---|
| below 30 | very easy |
| 30 to under 40 | easy |
| 40 to under 50 | medium |
| 50 to under 60 | difficult |
| 60 and above | very difficult |

The team's rule: **help-centre articles must score 40 or less** and contain
**no filler words**.

---

## Tasks

Work in `starter.py`, one task at a time. **Run the file after every task**,
printing your new variable to check it before moving on.

### Task 1: Split and clean the words (10 min)
1. Split `ARTICLE` into a list of words, `raw_words`.
2. Make a new list, `words`, where each word has its punctuation removed and
   is in lower case: `"Actually,"` becomes `"actually"`.

> Two string tools you haven't seen yet:
> - `text.split()` breaks a string into a list of words wherever there are
>   spaces or new lines.
> - `word.strip(".,!?")` removes those characters from both ends of a word.
>   You already know `strip()` without anything inside the brackets, which
>   removes spaces.

### Task 2: Count words and sentences (5 min)
- `word_count`: how many words there are
- `sentence_count`: how many sentences. A sentence ends where a word in
  `raw_words` ends with `.`, `!` or `?`.

### Task 3: Averages (5 min)
- words per sentence
- average word length, in letters

### Task 4: Long words and filler words (10 min)
- `long_words`: every word with at least `LONG_WORD_MIN_LETTERS` letters
- `fillers_found`: every word that appears in `FILLER_WORDS`
- the percentage of words that are long

### Task 5: The LIX score and reading level (10 min)
Work out the LIX score with the formula above, then use the table to decide
the reading level.

### Task 6: The longest words (5 min)
Find the `TOP_N` longest words, longest first.

### Task 7: Print the report (10 min)
Print the report shown in **Expected output** below. The verdict has three
possible outcomes:

| Situation | Verdict |
|---|---|
| LIX is 40 or less **and** no filler words | `ready to publish.` |
| LIX is 40 or less, but there are filler words | `readable, but cut the filler words.` |
| LIX is over 40 | `needs editing. Aim for a LIX of 40 or less.` |

Only print the filler-word section if any were found.

---

## Expected output

```text
===== READABILITY: HOW TO RESET YOUR PASSWORD =====
Words: 75
Sentences: 8
Words per sentence: 9.4
Average word length: 5.6 letters
Long words: 29 (39%)
LIX score: 48 (medium)

Longest 5 words:
  verification (12)
  instructions (12)
  difficulties (12)
  immediately (11)
  registered (10)

Filler words to cut (4):
  - simply
  - basically
  - actually
  - really

Verdict: needs editing. Aim for a LIX of 40 or less.
```

---

## Hints

Only open a hint if you're stuck for more than 5 minutes.

<details>
<summary>Hint 1: Cleaning every word at once</summary>

A list comprehension can call two methods in a row on each word:
`[word.strip(PUNCTUATION).lower() for word in raw_words]`
</details>

<details>
<summary>Hint 2: Finding where sentences end</summary>

A string can be indexed like a list. `word[-1]` is its last character.
Check `word[-1] in SENTENCE_ENDINGS` on the **raw** words, because the clean
words have lost their punctuation.
</details>

<details>
<summary>Hint 3: Average word length</summary>

Make a list of every word's length with a comprehension, `sum()` it, then
divide by the number of words.
</details>

<details>
<summary>Hint 4: The reading level</summary>

Use an `if` / `elif` / `else` chain. Start with the lowest band
(`if lix < 30:`) and work upwards, so each `elif` only needs one comparison.
</details>

<details>
<summary>Hint 5: Sorting words by length</summary>

Tuples sort by their first item. Build `(len(word), word)` tuples, sort them
with `reverse=True`, then slice off the first `TOP_N`.
</details>

<details>
<summary>Hint 6: The three-way verdict</summary>

`if lix <= TARGET_LIX and not fillers_found:` covers the first row of the
table. An empty list counts as `False`, so `not fillers_found` is `True` when
no filler words were found.
</details>

---

## Rules for your code

- Use the constants (`TARGET_LIX`, `LONG_WORD_MIN_LETTERS`, ...) instead of
  typing `40` or `7` in your calculations.
- Prefer list comprehensions for building lists; use `for` loops for printing.
- Use clear names: `word_count`, not `wc` or `x`.
- Use `:.1f` or `:.0f` in f-strings to round numbers for display.

## Check your work

1. Your output matches the expected output.
2. Change `TARGET_LIX` to `50`. The verdict should now be
   `readable, but cut the filler words.`

## Part 2: Be the editor (10 min)

Now use your tool the way the content team would. **Rewrite `ARTICLE` in
plain English** until the verdict says `ready to publish.`

Ideas that lower the score:
- Swap long words for short ones: "immediately" → "right away",
  "difficulties" → "problems".
- Split long sentences in two.
- Delete the filler words.

> One rewrite we tried scored **28 (very easy)**. Can you beat it without
> losing any of the instructions a customer needs?

Discuss: does a lower score always mean better writing? What would a
readability formula miss?

## Bonus (if you finish early)

- After a plain rewrite, the longest-words list can show `password` three
  times. Build a list of **unique** words with a `for` loop, `if ... not in`
  and `.append()`, and use it for the longest-words list.
- **Lexical diversity**: unique words divided by total words. A low number
  means the text repeats itself a lot.
- Check the article against a tuple of **jargon words** your team wants to
  avoid, such as `("authenticate", "credentials", "verification")`.
