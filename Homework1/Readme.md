# Name:- Jai Venkat Rayapureddy
# ID:-   700782045

# Q1. Regex

## Task: Write a regex to find

### 1. U.S. ZIP Codes (Disjunction + Token Boundaries)

Match `12345` **or** `12345-6789` **or** `12345 6789` (hyphen **or** space allowed for the +4 part). Make sure you only match whole tokens (not inside longer strings).

```regex
\b\d{5}(?:[- ]\d{4})?\b
```

**Explanation:**

- `\b` represents a word boundary.
- `\d{5}` matches exactly 5 digits.
- `[- ]` matches either a hyphen or a space.
- `\d{4}` matches exactly 4 digits.
- `(?: ... )?` makes the +4 part optional.


### 2. Negation in Disjunction (Word Start Rules)

Find all **words** that **do not** start with a capital letter. Words may include internal apostrophes/hyphens like `don’t`, `state-of-the-art`.

```regex
\b[a-z][A-Za-z]*(?:['’-][A-Za-z]+)*\b
```

**Explanation:**

- `\b` represents the beginning of a word.
- `[a-z]` makes sure the first letter is lowercase.
- `[A-Za-z]*` matches zero or more letters.
- `['’-]` allows an apostrophe or hyphen inside the word.
- `(?: ... )*` allows the apostrophe/hyphen part to occur zero or more times.


### 3. Convenient Aliases (Numbers, a Bit Richer)

Extract all numbers that may have an optional sign (`+`/`-`), optional thousands separators (commas), optional decimal part, and optional scientific notation.

```regex
[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?
```

**Explanation:**

- `[+-]?` allows an optional positive or negative sign.
- `\d{1,3}(?:,\d{3})+` handles numbers with commas.
- `|\d+` also allows numbers without commas.
- `(?:\.\d+)?` allows an optional decimal part.
- `(?:[eE][+-]?\d+)?` allows optional scientific notation.


### 4. More Disjunction (Spelling Variants)

Match any spelling of “email”: `email`, `e-mail`, or `e mail`. Accept either a **space** or a **hyphen** (including en-dash `–`) between `e` and `mail`, and be case-insensitive.

```regex
\be[-– ]?mail\b
```

Use case-insensitive matching in Python:

```python
re.findall(r"\be[-– ]?mail\b", text, re.IGNORECASE)
```

**Explanation:**

- `\b` represents a word boundary.
- `e` and `mail` match the two parts of the word.
- `[-– ]?` allows an optional hyphen, en-dash, or space.
- `re.IGNORECASE` makes the matching case-insensitive.


### 5. Wildcards, Optionality, Repetition (With Punctuation)

Match the interjection `go`, `goo`, `gooo`, … (one or more `o`), **as a word**, and allow an optional trailing punctuation mark `! . , ?`.

```regex
\bgo+[!.,?]?
```

**Explanation:**

- `\b` represents the beginning of a word.
- `g` matches the letter `g`.
- `o+` matches one or more `o` characters.
- `[!.,?]` matches one of the given punctuation marks.
- The final `?` makes the punctuation optional.


### 6. Anchors (Line/Sentence End With Quotes)

Match lines that **end with a question mark** possibly followed only by closing quotes/brackets like `")”’]` and spaces.

```regex
.*\?["')”’\]]*\s*$
```

**Explanation:**

- `.*` matches the text before the question mark.
- `\?` matches the question mark.
- `["')”’\]]*` allows closing quotes or brackets after the question mark.
- `\s*` allows spaces at the end.
- `$` makes sure the pattern reaches the end of the line.



# Q2. Manual BPE on a Toy Corpus

## 2.1 Manual BPE

### Question

Using the following corpus:

```text
low low low low low lowest lowest newer newer newer newer newer newer
wider wider wider new new
```

1. Add the end-of-word marker `_` and write the initial vocabulary (characters + `_`).
2. Compute bigram counts and perform the first three merges by hand.
   - Step 1: Most frequent pair → merge → updated corpus snippet.
   - Step 2: Repeat.
   - Step 3: Repeat.
3. After each merge, list the new token and the updated vocabulary.

### Answer

#### Initial Vocabulary

After adding the end-of-word marker `_`:

```text
low     → l o w _
lowest  → l o w e s t _
newer   → n e w e r _
wider   → w i d e r _
new     → n e w _
```

Initial vocabulary:

```text
{_, d, e, i, l, n, o, r, s, t, w}
```

Vocabulary size = `11`

#### Bigram Counts

The main bigram counts are:

```text
(e, r) = 9
(r, _) = 9
(n, e) = 8
(e, w) = 8
(l, o) = 7
(o, w) = 7
(w, _) = 7
```

There is a tie between `(e, r)` and `(r, _)`, with a count of 9. For the manual calculation, `(e, r)` is selected first.

#### Step 1

Most frequent pair:

```text
(e, r) = 9
```

Merge:

```text
e + r → er
```

Updated corpus snippet:

```text
newer → n e w er _
wider → w i d er _
```

New token: `er`

Updated vocabulary:

```text
{_, d, e, i, l, n, o, r, s, t, w, er}
```

Vocabulary size = `12`

#### Step 2

Most frequent pair:

```text
(er, _) = 9
```

Merge:

```text
er + _ → er_
```

Updated corpus snippet:

```text
newer → n e w er_
wider → w i d er_
```

New token: `er_`

Updated vocabulary:

```text
{_, d, e, i, l, n, o, r, s, t, w, er, er_}
```

Vocabulary size = `13`

#### Step 3

The next highest pairs `(n, e)` and `(e, w)` both have a count of 8. For this step, `(n, e)` is selected.

```text
(n, e) = 8
```

Merge:

```text
n + e → ne
```

Updated corpus snippet:

```text
newer → ne w er_
new   → ne w _
```

New token: `ne`

Updated vocabulary:

```text
{_, d, e, i, l, n, o, r, s, t, w, er, er_, ne}
```

Vocabulary size = `14`


## 2.2 Code a Mini-BPE Learner

### Question

1. Use the classroom code or your own code to learn BPE merges for the toy corpus.
   - Print the top pair at each step.
   - Print the evolving vocabulary size.
2. Segment the following words:
   - `new`
   - `newer`
   - `lowest`
   - `widest`
   - One invented word such as `newestest`
3. In 5–6 sentences, explain:
   - How subword tokens solve the OOV (out-of-vocabulary) problem.
   - One example where a subword matches a meaningful morpheme, such as `er_`.

### Answer

The mini-BPE learner is implemented in the separate Python file `q2_bpe.py`.

#### Segmentation Results

Initial Vocabulary: ['_', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'w']
Initial Vocabulary Size: 11

Step 1
Top Pair: ('e', 'r')
Frequency: 9
New Token: er
Vocabulary Size: 12

Step 2
Top Pair: ('er', '_')
Frequency: 9
New Token: er_
Vocabulary Size: 13

Step 3
Top Pair: ('n', 'e')
Frequency: 8
New Token: ne
Vocabulary Size: 14

Step 4
Top Pair: ('ne', 'w')
Frequency: 8
New Token: new
Vocabulary Size: 15

Step 5
Top Pair: ('l', 'o')
Frequency: 7
New Token: lo
Vocabulary Size: 16

Step 6
Top Pair: ('lo', 'w')
Frequency: 7
New Token: low
Vocabulary Size: 17

Step 7
Top Pair: ('new', 'er_')
Frequency: 6
New Token: newer_
Vocabulary Size: 18

Step 8
Top Pair: ('low', '_')
Frequency: 5
New Token: low_
Vocabulary Size: 19

Step 9
Top Pair: ('w', 'i')
Frequency: 3
New Token: wi
Vocabulary Size: 20

Step 10
Top Pair: ('wi', 'd')
Frequency: 3
New Token: wid
Vocabulary Size: 21

Learned Merges
--------------
1 ('e', 'r')
2 ('er', '_')
3 ('n', 'e')
4 ('ne', 'w')
5 ('l', 'o')
6 ('lo', 'w')
7 ('new', 'er_')
8 ('low', '_')
9 ('w', 'i')
10 ('wi', 'd')

Word Segmentation
-----------------
new -> new | _
newer -> newer_
lowest -> low | e | s | t | _
widest -> wid | e | s | t | _
newestest -> new | e | s | t | e | s | t | _

#### Explanation

BPE helps solve the out-of-vocabulary problem by splitting words into smaller subword tokens. If a complete word is not present in the training data, it can still be represented using smaller tokens that were learned. For example, `widest` is not present in the given corpus, but BPE can still split it into smaller pieces instead of treating the complete word as unknown. Some learned subwords can also match meaningful parts of words. For example, `er_` can represent the `er` ending found in words such as `newer` and `wider`. However, BPE learns merges based on frequency, so every learned subword may not have a linguistic meaning.


## 2.3 BPE on My Own Paragraph

### Question

Choose a short paragraph of 4–6 sentences in your own language or English.

1. Train BPE on the paragraph.
   - Use `_` as the end-of-word marker.
   - Learn at least 30 merges.
2. Show:
   - Five most frequent merges.
   - Five longest resulting subword tokens.
3. Segment five different words from the paragraph.
   - Include one rare word.
   - Include one derived or inflected word.
4. Write a 5–8 sentence reflection explaining:
   - What kinds of subwords were learned.
   - Two concrete pros/cons of subword tokenization.

### Answer

#### Paragraph

```text
Machine learning helps computers learn patterns from data.
Machine learning models can solve different types of problems.
Learning from larger datasets can improve model performance.
Natural language processing helps computers understand human language.
Intelligent systems can use language models to process information.
```

The BPE learner was trained using `_` as the end-of-word marker for at least 30 merges.

#### Five Most Frequent Merges

```text
('s', '_') Frequency: 12
('e', '_') Frequency: 9
('a', 'n') Frequency: 9
('i', 'n') Frequency: 8
('e', 'r') Frequency: 7
```

#### Five Longest Subword Tokens

```text
language_
learning_
languag
langua
langu
```

#### Word Segmentation

```text
learning -> learning_
computers -> c | o | m | p | u | ter | s_
language -> language_
models -> model | s_
intelligent -> in | t | el | l | i | g | e | n | t | _
```

#### Reflection

The BPE model learned different types of tokens, including individual characters and larger parts of words. Some frequently occurring character sequences were combined into larger subwords. Some of these subwords may represent stems or suffixes, while others are created mainly because they occur frequently in the paragraph. One advantage of BPE is that it can represent rare or unseen words using smaller known tokens. It can also reduce the need to keep every possible word in the vocabulary. One disadvantage is that some learned subwords may not have a clear linguistic meaning. Rare words can also be divided into several smaller tokens.

## Q3. Bayes Rule Applied to Text

The classification is based on:

P(c|d) = [P(d|c) × P(c)] / P(d)

where `c` represents a class and `d` represents a document.

### 1. Explain in your own words what each term means: P(c), P(d|c), and P(c|d).

**Answer:**

**P(c) - Prior Probability**

P(c) is the probability of class `c` before looking at the document.

For example, if we are classifying emails as spam or not spam, P(spam) represents the probability that an email is spam based on the training data.

**P(d|c) - Likelihood**

P(d|c) is the probability of observing document `d` when it belongs to class `c`.

For example, P(document|spam) tells us how likely the words in the document are to appear in a spam email.

**P(c|d) - Posterior Probability**

P(c|d) is the probability that document `d` belongs to class `c` after looking at the document.

For example, P(spam|document) tells us how likely the email is to be spam after considering the words in the document.


### 2. Why can the denominator P(d) be ignored when comparing classes?

**Answer:**

When we compare different classes for the same document, P(d) remains the same for every class.

For example:

P(spam|d) = [P(d|spam) × P(spam)] / P(d)

P(not spam|d) = [P(d|not spam) × P(not spam)] / P(d)

Since P(d) is the same in both calculations, it does not affect which class has the higher probability.

Therefore, we can ignore P(d) and compare only:

P(c) × P(d|c)

The class with the highest value is selected as the predicted class.


## Q4. Add-1 Smoothing

Given:

- P(-) = 3/5
- P(+) = 2/5
- Vocabulary size (V) = 20
- Total token count in the negative class = 14

For Add-1 smoothing, the likelihood is calculated using:

P(word|class) = (Count(word, class) + 1) / (Total tokens in class + V)


### 1. For the negative class, the total token count is 14. Compute the denominator for likelihood estimation using Add-1 smoothing.

**Answer:**

Denominator = Total token count + Vocabulary size

Denominator = 14 + 20

Denominator = 34

Therefore, the denominator for the negative class is **34**.


### 2. Compute P(predictable|-) if the word "predictable" occurs 2 times in the negative documents.

**Answer:**

Using Add-1 smoothing:

P(predictable|-) = (Count(predictable, -) + 1) / 34

P(predictable|-) = (2 + 1) / 34

P(predictable|-) = 3/34

P(predictable|-) ≈ 0.0882

Therefore:

**P(predictable|-) = 3/34 ≈ 0.0882**


### 3. Compute P(fun|-) if "fun" never appeared in any negative documents.

**Answer:**

Since "fun" never appeared in the negative documents, its count is 0.

Using Add-1 smoothing:

P(fun|-) = (Count(fun, -) + 1) / 34

P(fun|-) = (0 + 1) / 34

P(fun|-) = 1/34

P(fun|-) ≈ 0.0294

Therefore:

**P(fun|-) = 1/34 ≈ 0.0294**


## Q5. Programming Question

### 1. Tokenize a Paragraph

**Paragraph:**

I live in New York City. I'm studying natural language processing.
Machine learning is very interesting, but it isn't always easy.
I want to work in artificial intelligence.

### Naive Space-Based Tokenization

**Output:**

[
'I', 'live', 'in', 'New', 'York', 'City.', "I'm", 'studying',
'natural', 'language', 'processing.', 'Machine', 'learning',
'is', 'very', 'interesting,', 'but', 'it', "isn't", 'always',
'easy.', 'I', 'want', 'to', 'work', 'in', 'artificial', 'intelligence.'
]

**Answer:**

Naive space-based tokenization splits the text only when it finds a space.
Because of this, punctuation remains attached to some words.

Examples:

- `City.` keeps the period.
- `processing.` keeps the period.
- `interesting,` keeps the comma.
- `easy.` keeps the period.
- `I'm` and `isn't` are not separated.


### Manually Corrected Tokenization

**Output:**

[
'I', 'live', 'in', 'New', 'York', 'City', '.',
'I', "'m", 'studying', 'natural', 'language', 'processing', '.',
'Machine', 'learning', 'is', 'very', 'interesting', ',',
'but', 'it', 'is', "n't", 'always', 'easy', '.',
'I', 'want', 'to', 'work', 'in', 'artificial', 'intelligence', '.'
]

**Answer:**

In the manually corrected version, punctuation and contractions are
separated into individual tokens.

Some differences are:

- `City.` → `City`, `.`
- `processing.` → `processing`, `.`
- `interesting,` → `interesting`, `,`
- `easy.` → `easy`, `.`
- `I'm` → `I`, `'m`
- `isn't` → `is`, `n't`


### 2. Compare with an NLP Tool

**Tool Used:** NLTK `word_tokenize()`

**NLTK Output:**

[
'I', 'live', 'in', 'New', 'York', 'City', '.',
'I', "'m", 'studying', 'natural', 'language', 'processing', '.',
'Machine', 'learning', 'is', 'very', 'interesting', ',',
'but', 'it', 'is', "n't", 'always', 'easy', '.',
'I', 'want', 'to', 'work', 'in', 'artificial', 'intelligence', '.'
]

**Answer:**

The NLTK output is the same as my manually corrected tokenization for
this paragraph.

NLTK correctly separates punctuation from words and also splits
contractions such as `I'm` into `I` and `'m`, and `isn't` into
`is` and `n't`.

The main difference between naive tokenization and NLTK is that naive
tokenization only uses spaces, while NLTK applies tokenization rules for
punctuation and contractions.


### 3. Multiword Expressions

**1. New York City**

`New York City` is a place name. The three words together represent one
location, so they can be treated as one expression.

Representation:

`New_York_City`

**2. Natural Language Processing**

`Natural Language Processing` is a technical term that represents a
specific field in artificial intelligence.

Representation:

`Natural_Language_Processing`

**3. Machine Learning**

`Machine Learning` is a common technical term where the two words
together represent one concept.

Representation:

`Machine_Learning`


### 4. Reflection

**Answer:**

The hardest part of tokenization was handling punctuation and
contractions correctly. Space-based tokenization is simple, but it keeps
punctuation attached to words. Contractions such as `I'm` and `isn't`
also need special handling because one written word can produce multiple
tokens. NLTK handled these cases correctly for this paragraph. Multiword
expressions also make tokenization more difficult because several words
can represent one meaning. Overall, punctuation, contractions, morphology,
and multiword expressions can make tokenization more challenging.
