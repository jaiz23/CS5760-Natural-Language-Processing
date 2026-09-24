# Q5 - Multi-Class Confusion Matrix


# Confusion matrix
matrix = [
    [5, 10, 5],
    [15, 20, 10],
    [0, 15, 10]
]

classes = ["Cat", "Dog", "Rabbit"]

precisions = []
recalls = []

print("Per-Class Metrics:\n")

for i in range(len(classes)):

    # True Positive
    tp = matrix[i][i]

    # Total predicted as this class
    predicted_total = sum(matrix[i])

    # Total actual examples of this class
    actual_total = sum(row[i] for row in matrix)

    # Calculate precision and recall
    precision = tp / predicted_total
    recall = tp / actual_total

    precisions.append(precision)
    recalls.append(recall)

    print(f"{classes[i]}:")
    print(f"Precision = {precision:.4f}")
    print(f"Recall = {recall:.4f}")
    print()

# Macro averages
macro_precision = sum(precisions) / len(precisions)
macro_recall = sum(recalls) / len(recalls)

# Micro averages
total_tp = sum(matrix[i][i] for i in range(len(classes)))
total_examples = sum(sum(row) for row in matrix)

micro_precision = total_tp / total_examples
micro_recall = total_tp / total_examples

print(f"Macro-Averaged Precision = {macro_precision:.4f}")
print(f"Macro-Averaged Recall = {macro_recall:.4f}")
print()

print(f"Micro-Averaged Precision = {micro_precision:.4f}")
print(f"Micro-Averaged Recall = {micro_recall:.4f}")