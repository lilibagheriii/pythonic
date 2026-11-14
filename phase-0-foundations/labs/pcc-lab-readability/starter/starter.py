from string import punctuation

ARTICLE_TITLE = "how to reset your password"
LONG_WORD_MIN_LETTERS = 7      # LIX counts words with more than 6 letters
TARGET_LIX = 40                # help-centre articles should be "easy"
TOP_N = 5
PUNCTUATION = ".,!?:;\"()"
SENTENCE_ENDINGS = ".!?"

# Words that add length but no meaning.
FILLER_WORDS = ("actually", "basically", "really", "very", "just", "simply")

ARTICLE = """Forgot your password? Don't worry, it happens to everyone.
Go to the sign-in page and simply select the reset link. We will basically
send a verification message to your registered email address immediately.
Open the message and follow the instructions. Your new password must
contain at least twelve characters, including numbers and symbols.
Actually, we really recommend using a password manager for additional
security. If you still experience difficulties, please contact our
customer support team."""

# TODO Task 1: split the text into words, then clean them
words = ARTICLE.split()
print(words)
words_nopunc= [word.strip(punctuation) for word in words]
print(words_nopunc)

# TODO Task 2: count words and sentences
word_count = len(words)
print(word_count)


sentence_count= 0
for char in ARTICLE:
    if char in SENTENCE_ENDINGS:
        sentence_count += 1
        print(sentence_count)


# TODO Task 3: words per sentence and average word length

words_per_sentence = word_count / sentence_count
print(words_per_sentence)

lengths = [len(word) for word in words_nopunc]
average_word_length = sum(lengths) / word_count
print(average_word_length)

# TODO Task 4: long words and filler words
long_words = [
    word
    for word in words
    if len(word) >= LONG_WORD_MIN_LETTERS
]

print(long_words)
# TODO Task 5: LIX score and reading level
# (words / sentences) +  (long words * 100 / words)
lix = words_per_sentence + (len(long_words) * 100 / word_count)
print(f"{lix:.2f}")


# TODO Task 6: the longest words
longest_word_length = max(len(word) for word in words_nopunc)
print(longest_word_length)
longest_words = [
    word for word in words
    if len(word) >= 12
]
print(longest_words)
# TODO Task 7: print the report
