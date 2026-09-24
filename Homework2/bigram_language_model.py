# Bigram Language Model


from collections import Counter

# Training corpus
corpus = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "deep", "learning", "</s>"],
    ["<s>", "deep", "learning", "is", "fun", "</s>"]
]

# Count unigrams
unigram_counts = Counter()

# Count bigrams
bigram_counts = Counter()

for sentence in corpus:

    # Count each word
    unigram_counts.update(sentence)

    # Count each pair of consecutive words
    for i in range(len(sentence) - 1):
        bigram = (sentence[i], sentence[i + 1])
        bigram_counts[bigram] += 1


print("Unigram Counts:")
for word, count in unigram_counts.items():
    print(word, ":", count)


print("\nBigram Counts:")
for bigram, count in bigram_counts.items():
    print(bigram, ":", count)


# Calculate bigram probability using MLE
def bigram_probability(previous_word, current_word):

    pair = (previous_word, current_word)

    bigram_count = bigram_counts[pair]
    previous_count = unigram_counts[previous_word]

    if previous_count == 0:
        return 0

    return bigram_count / previous_count


print("\nBigram Probabilities:")

for bigram in bigram_counts:

    probability = bigram_probability(
        bigram[0],
        bigram[1]
    )

    print(
        f"P({bigram[1]} | {bigram[0]}) = "
        f"{probability:.4f}"
    )


# Calculate probability of a sentence
def sentence_probability(sentence):

    words = sentence.split()

    probability = 1.0

    for i in range(len(words) - 1):

        bigram_prob = bigram_probability(
            words[i],
            words[i + 1]
        )

        probability *= bigram_prob

    return probability


# Test sentences
sentence1 = "<s> I love NLP </s>"
sentence2 = "<s> I love deep learning </s>"

prob1 = sentence_probability(sentence1)
prob2 = sentence_probability(sentence2)

print("\nSentence Probabilities:")

print(f"S1: {sentence1}")
print(f"Probability = {prob1:.4f}")

print()

print(f"S2: {sentence2}")
print(f"Probability = {prob2:.4f}")


# Compare the sentences
print("\nModel Preference:")

if prob1 > prob2:

    print("The model prefers Sentence 1.")
    print(
        "Sentence 1 has a higher probability "
        "than Sentence 2."
    )

elif prob2 > prob1:

    print("The model prefers Sentence 2.")
    print(
        "Sentence 2 has a higher probability "
        "than Sentence 1."
    )

else:

    print("Both sentences have the same probability.")