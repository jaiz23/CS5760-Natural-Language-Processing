# CS5760 Natural Language Processing
## Homework 2

### Student Information

**Name:** Jai Venkat Rayapureddy
**Course:** CS5760 Natural Language Processing  
**Semester:** Fall 2026

---

# Part I: Writing Calculation

## Q1. Worked Example Document Classification

Test document:

`predictable no fun`

Using Add-1 smoothing:

P(w|c) = (count(w,c) + 1) / (total words in class + |V|)

Given:

P(-) = 3/5  
P(+) = 2/5  
Vocabulary size = 20

Negative class total = 14  
Positive class total = 9

### 1. Negative Class Score

For the negative class:

P(predictable|-) = (1 + 1) / (14 + 20)

= 2/34

P(no|-) = (1 + 1) / (14 + 20)

= 2/34

P(fun|-) = (0 + 1) / (14 + 20)

= 1/34

Now calculate the negative class score:

P(-) × P(predictable|-) × P(no|-) × P(fun|-)

= 3/5 × 2/34 × 2/34 × 1/34

≈ 0.000061

Therefore,

**Negative Score ≈ 6.1 × 10^-5**

### 2. Positive Class Score

For the positive class:

P(predictable|+) = (0 + 1) / (9 + 20)

= 1/29

P(no|+) = (0 + 1) / (9 + 20)

= 1/29

P(fun|+) = (1 + 1) / (9 + 20)

= 2/29

Now calculate the positive class score:

P(+) × P(predictable|+) × P(no|+) × P(fun|+)

= 2/5 × 1/29 × 1/29 × 2/29

≈ 0.0000328

Therefore,

**Positive Score ≈ 3.2 × 10^-5**

### 3. Which class should the system assign?

The negative score is higher than the positive score:

6.1 × 10^-5 > 3.2 × 10^-5

Therefore, the system assigns the document to the:

**Negative Class (-)**

---

## Q2. Harms of Classification

### 1. Define representational harm and explain how the Kiritchenko & Mohammad (2018) study demonstrates this type of harm.

**Answer:**

Representational harm happens when a system represents a social group in a negative or unfair way and can reinforce stereotypes about that group.

Kiritchenko and Mohammad (2018) tested sentiment analysis systems using pairs of sentences that were almost identical except for names associated with different groups. For example, they compared sentences containing African American-associated names with sentences containing European American-associated names.

The study found that some systems assigned lower sentiment and more negative emotions to sentences containing African American-associated names. This can reinforce negative stereotypes and cause unfair representation of a social group.

### 2. What is one risk of censorship in toxicity classification systems?

**Answer:**

A toxicity classifier may incorrectly classify non-toxic text as toxic simply because it contains words referring to minority identities.

For example, words such as "gay" or "blind" may cause a classifier to incorrectly flag a sentence. This can result in legitimate content being removed or made less visible online. It can also discourage people from talking about their own identities or communities.

### 3. Give one reason why classifiers may perform worse on African American English or Indian English.

**Answer:**

One reason is that the training data may not contain enough examples from different varieties of English.

If a classifier is trained mostly on Standard American English, it may not learn the vocabulary, grammar, and language patterns used in African American English or Indian English. Because of this lack of representative training data, the classifier may make more errors on these varieties.

---

## Q3. Bigram Probabilities and the Zero-Probability Problem

The bigram probability formula is:

P(wᵢ|wᵢ₋₁) = C(wᵢ₋₁, wᵢ) / C(wᵢ₋₁)

### 1. Bigram Sentence Probabilities

### Sentence S1

`<s> I love NLP </s>`

The probability is:

P(S1) = P(I|<s>) × P(love|I) × P(NLP|love) × P(</s>|NLP)

Calculate each probability:

P(I|<s>) = 2/3

P(love|I) = 2/2 = 1

P(NLP|love) = 1/2

P(</s>|NLP) = 1/1 = 1

Therefore:

P(S1) = 2/3 × 1 × 1/2 × 1

P(S1) = 1/3

**P(S1) ≈ 0.3333**

---

### Sentence S2

`<s> I love deep learning </s>`

The probability is:

P(S2) = P(I|<s>) × P(love|I) × P(deep|love)
× P(learning|deep) × P(</s>|learning)

Calculate each probability:

P(I|<s>) = 2/3

P(love|I) = 2/2 = 1

P(deep|love) = 1/2

P(learning|deep) = 2/2 = 1

P(</s>|learning) = 1/2

Therefore:

P(S2) = 2/3 × 1 × 1/2 × 1 × 1/2

P(S2) = 1/6

**P(S2) ≈ 0.1667**

### Which sentence is more probable?

P(S1) = 0.3333

P(S2) = 0.1667

Since:

0.3333 > 0.1667

The bigram model prefers:

**S1: `<s> I love NLP </s>`**

---

## Q3.2 Zero-Probability Problem

### Compute P(noodle|ate) using MLE.

Given:

ate → lunch = 6  
ate → dinner = 3  
ate → a = 2  
ate → the = 1

Total:

C(ate) = 6 + 3 + 2 + 1 = 12

The bigram `ate noodle` never appeared.

Therefore:

C(ate, noodle) = 0

Using MLE:

P(noodle|ate) = C(ate, noodle) / C(ate)

P(noodle|ate) = 0/12

**P(noodle|ate) = 0**

### Why does zero probability create a problem?

**Answer:**

The probability of a sentence in a bigram model is calculated by multiplying all of its bigram probabilities. If one bigram has a probability of 0, the probability of the entire sentence becomes 0.

This is a problem because a valid sentence may contain a bigram that was simply not present in the training data. Zero probabilities also cause problems when calculating perplexity because the model assigns no probability to the sentence.

### Apply Laplace Smoothing

The Add-1 smoothing formula is:

P(w|h) = (C(h,w) + 1) / (C(h) + V)

Given:

C(ate, noodle) = 0  
C(ate) = 12  
V = 10

Therefore:

P(noodle|ate) = (0 + 1) / (12 + 10)

= 1/22

≈ 0.0455

Therefore,

**P(noodle|ate) ≈ 0.0455**

---

## Q4. Backoff Model

Training corpus:

`<s> I like cats </s>`

`<s> I like dogs </s>`

`<s> You like cats </s>`

### 1. Compute P(cats|I, like)

The trigram `I like cats` occurs once.

The history `I like` occurs twice:

`I like cats`

`I like dogs`

Therefore:

P(cats|I, like) = C(I like cats) / C(I like)

= 1/2

**P(cats|I, like) = 0.5**

---

### 2. Compute P(dogs|You, like) using trigram → bigram backoff.

First try the trigram:

`You like dogs`

This trigram does not appear in the training corpus.

Therefore:

P(dogs|You, like) = 0

Since the trigram is unseen, we back off to the bigram:

P(dogs|like)

After the word `like`, we have:

cats = 2 times  
dogs = 1 time

Total occurrences after `like` = 3.

Therefore:

P(dogs|like) = 1/3

≈ 0.3333

Using backoff:

**P(dogs|You, like) ≈ 0.3333**

---

### 3. Why is backoff necessary?

**Answer:**

Backoff is necessary because some higher-order n-grams may not appear in the training data. If we only use the trigram model, an unseen trigram would receive a probability of 0.

Instead of immediately assigning zero probability, backoff uses a lower-order model. It first tries the trigram, then the bigram, and finally the unigram if necessary. This allows the model to estimate probabilities for combinations that were not seen in the training data.

---

## Q5. Evaluation Metrics from a Multi-Class Confusion Matrix

Given confusion matrix:

| System / Gold | Cat | Dog | Rabbit |
|---|---:|---:|---:|
| Cat | 5 | 10 | 5 |
| Dog | 15 | 20 | 10 |
| Rabbit | 0 | 15 | 10 |

The formulas are:

Precision = TP / (TP + FP)

Recall = TP / (TP + FN)

---

### 1. Per-Class Metrics

### Cat

True Positive:

TP = 5

Total predicted as Cat:

5 + 10 + 5 = 20

Precision:

Precision(Cat) = 5/20

**Precision(Cat) = 0.25**

Total actual Cat:

5 + 15 + 0 = 20

Recall:

Recall(Cat) = 5/20

**Recall(Cat) = 0.25**

---

### Dog

True Positive:

TP = 20

Total predicted as Dog:

15 + 20 + 10 = 45

Precision:

Precision(Dog) = 20/45

**Precision(Dog) ≈ 0.4444**

Total actual Dog:

10 + 20 + 15 = 45

Recall:

Recall(Dog) = 20/45

**Recall(Dog) ≈ 0.4444**

---

### Rabbit

True Positive:

TP = 10

Total predicted as Rabbit:

0 + 15 + 10 = 25

Precision:

Precision(Rabbit) = 10/25

**Precision(Rabbit) = 0.40**

Total actual Rabbit:

5 + 10 + 10 = 25

Recall:

Recall(Rabbit) = 10/25

**Recall(Rabbit) = 0.40**

---

## 2. Macro vs. Micro Averaging

### Macro-Averaged Precision

Macro Precision = (0.25 + 0.4444 + 0.40) / 3

= 1.0944 / 3

**Macro Precision ≈ 0.3648**

### Macro-Averaged Recall

Macro Recall = (0.25 + 0.4444 + 0.40) / 3

**Macro Recall ≈ 0.3648**

---

### Micro-Averaged Precision

Total correct predictions:

5 + 20 + 10 = 35

Total predictions:

90

Micro Precision = 35/90

**Micro Precision ≈ 0.3889**

### Micro-Averaged Recall

Micro Recall = 35/90

**Micro Recall ≈ 0.3889**

---

### Difference Between Macro and Micro Averaging

**Answer:**

Macro averaging calculates precision or recall separately for each class and then takes the average. This gives equal importance to every class regardless of how many examples each class contains.

Micro averaging combines the results from all classes before calculating the metric. Therefore, classes with more examples have more influence on the final result.

---

## Q5.3 Programming Implementation

The Python implementation is available in:

`q5_confusion_matrix.py`

The program calculates:

- Precision for each class
- Recall for each class
- Macro-averaged precision and recall
- Micro-averaged precision and recall

### Output

```text
Per-Class Metrics:

Cat:
Precision = 0.2500
Recall = 0.2500

Dog:
Precision = 0.4444
Recall = 0.4444

Rabbit:
Precision = 0.4000
Recall = 0.4000

Macro-Averaged Precision = 0.3648
Macro-Averaged Recall = 0.3648

Micro-Averaged Precision = 0.3889
Micro-Averaged Recall = 0.3889
```

---

# Part II: Programming

## Q1. Bigram Language Model Implementation

Training corpus:

`<s> I love NLP </s>`

`<s> I love deep learning </s>`

`<s> deep learning is fun </s>`

The program:

1. Reads the training corpus.
2. Computes unigram counts.
3. Computes bigram counts.
4. Calculates bigram probabilities using MLE.
5. Calculates sentence probabilities.
6. Compares the two test sentences.

### Bigram Probabilities Used

P(I|<s>) = 2/3

P(deep|<s>) = 1/3

P(love|I) = 1

P(NLP|love) = 1/2

P(deep|love) = 1/2

P(learning|deep) = 1

P(</s>|NLP) = 1

P(</s>|learning) = 1/2

P(is|learning) = 1/2

P(fun|is) = 1

P(</s>|fun) = 1

---

### Sentence 1

`<s> I love NLP </s>`

P(S1) = 2/3 × 1 × 1/2 × 1

**P(S1) ≈ 0.3333**

### Sentence 2

`<s> I love deep learning </s>`

P(S2) = 2/3 × 1 × 1/2 × 1 × 1/2

**P(S2) ≈ 0.1667**


### Output

Unigram Counts:
<s> : 3
I : 2
love : 2
NLP : 1
</s> : 3
deep : 2
learning : 2
is : 1
fun : 1

Bigram Counts:
('<s>', 'I') : 2
('I', 'love') : 2
('love', 'NLP') : 1
('NLP', '</s>') : 1
('love', 'deep') : 1
('deep', 'learning') : 2
('learning', '</s>') : 1
('<s>', 'deep') : 1
('learning', 'is') : 1
('is', 'fun') : 1
('fun', '</s>') : 1

Bigram Probabilities:
P(I | <s>) = 0.6667
P(love | I) = 1.0000
P(NLP | love) = 0.5000
P(</s> | NLP) = 1.0000
P(deep | love) = 0.5000
P(learning | deep) = 1.0000
P(</s> | learning) = 0.5000
P(deep | <s>) = 0.3333
P(is | learning) = 0.5000
P(fun | is) = 1.0000
P(</s> | fun) = 1.0000

Sentence Probabilities:
S1: <s> I love NLP </s>
Probability = 0.3333

S2: <s> I love deep learning </s>
Probability = 0.1667

### Which sentence does the model prefer?

**Answer:**

The model prefers:

`<s> I love NLP </s>`

because its probability is approximately 0.3333, which is greater than the probability of the second sentence, approximately 0.1667.




