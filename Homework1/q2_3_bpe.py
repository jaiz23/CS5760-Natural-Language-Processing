from collections import Counter

# English paragraph for Q2.3
text = """
Machine learning helps computers learn patterns from data.
Machine learning models can solve different types of problems.
Learning from larger datasets can improve model performance.
Natural language processing helps computers understand human language.
Intelligent systems can use language models to process information.
"""

# Basic cleanup
text = text.lower()
text = text.replace(".", "")

# Count word frequencies
word_freq = Counter(text.split())

# Convert each word into characters and add "_" as end-of-word marker
corpus = {}

for word, freq in word_freq.items():
    tokens = tuple(list(word) + ["_"])
    corpus[tokens] = freq


# Count adjacent token pairs
def get_pair_counts(corpus):
    pair_counts = Counter()

    for tokens, freq in corpus.items():
        for i in range(len(tokens) - 1):
            pair = (tokens[i], tokens[i + 1])
            pair_counts[pair] += freq

    return pair_counts


# Merge a selected pair
def merge_pair(corpus, pair):
    new_corpus = {}

    for tokens, freq in corpus.items():
        new_tokens = []
        i = 0

        while i < len(tokens):

            if (
                i < len(tokens) - 1
                and tokens[i] == pair[0]
                and tokens[i + 1] == pair[1]
            ):
                new_tokens.append(tokens[i] + tokens[i + 1])
                i += 2

            else:
                new_tokens.append(tokens[i])
                i += 1

        new_corpus[tuple(new_tokens)] = freq

    return new_corpus


# Initial vocabulary
vocabulary = set()

for tokens in corpus:
    vocabulary.update(tokens)

print("Initial Vocabulary Size:", len(vocabulary))
print()


# Learn at least 30 merges
number_of_merges = 30

merges = []
merge_info = []

for step in range(number_of_merges):

    pair_counts = get_pair_counts(corpus)

    if not pair_counts:
        break

    best_pair, count = pair_counts.most_common(1)[0]

    merges.append(best_pair)
    merge_info.append((best_pair, count))

    corpus = merge_pair(corpus, best_pair)

    new_token = best_pair[0] + best_pair[1]
    vocabulary.add(new_token)

    print("Step", step + 1)
    print("Top Pair:", best_pair)
    print("Frequency:", count)
    print("New Token:", new_token)
    print("Vocabulary Size:", len(vocabulary))
    print()


# Show five most frequent merges
print("Five Most Frequent Merges")
print("-------------------------")

top_five_merges = sorted(
    merge_info,
    key=lambda x: x[1],
    reverse=True
)[:5]

for pair, count in top_five_merges:
    print(pair, "Frequency:", count)

print()


# Show five longest subword tokens
print("Five Longest Subword Tokens")
print("---------------------------")

longest_tokens = sorted(
    vocabulary,
    key=len,
    reverse=True
)[:5]

for token in longest_tokens:
    print(token)

print()


# Segment a word using learned merges
def segment_word(word, merges):

    tokens = list(word.lower()) + ["_"]

    for pair in merges:
        new_tokens = []
        i = 0

        while i < len(tokens):

            if (
                i < len(tokens) - 1
                and tokens[i] == pair[0]
                and tokens[i + 1] == pair[1]
            ):
                new_tokens.append(tokens[i] + tokens[i + 1])
                i += 2

            else:
                new_tokens.append(tokens[i])
                i += 1

        tokens = new_tokens

    return tokens


# Five words from the paragraph
test_words = [
    "learning",
    "computers",
    "language",
    "models",
    "intelligent"
]

print("Word Segmentation")
print("-----------------")

for word in test_words:
    tokens = segment_word(word, merges)
    print(word, "->", " | ".join(tokens))