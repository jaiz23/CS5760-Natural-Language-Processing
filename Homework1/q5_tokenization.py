import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer resources
nltk.download("punkt")
nltk.download("punkt_tab")

# Paragraph used for tokenization
text = """I live in New York City. I'm studying natural language processing.
Machine learning is very interesting, but it isn't always easy.
I want to work in artificial intelligence."""

# ---------------------------------------------------
# 1. Naive Space-Based Tokenization
# ---------------------------------------------------

naive_tokens = text.split()

print("Naive Space-Based Tokenization:")
print(naive_tokens)


# ---------------------------------------------------
# 2. Manually Corrected Tokenization
# ---------------------------------------------------

manual_tokens = [
    'I', 'live', 'in', 'New', 'York', 'City', '.',
    'I', "'m", 'studying', 'natural', 'language', 'processing', '.',
    'Machine', 'learning', 'is', 'very', 'interesting', ',',
    'but', 'it', 'is', "n't", 'always', 'easy', '.',
    'I', 'want', 'to', 'work', 'in', 'artificial', 'intelligence', '.'
]

print("\nManually Corrected Tokenization:")
print(manual_tokens)


# ---------------------------------------------------
# 3. NLTK Tokenization
# ---------------------------------------------------

nltk_tokens = word_tokenize(text)

print("\nNLTK Tokenization:")
print(nltk_tokens)


# ---------------------------------------------------
# 4. Multiword Expressions
# ---------------------------------------------------

mwes = [
    "New York City",
    "Natural Language Processing",
    "Machine Learning"
]

print("\nMultiword Expressions:")

for mwe in mwes:
    print(mwe)