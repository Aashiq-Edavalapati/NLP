import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity

# Documents and query
docs = [
    "walking common activity",
    "running walking forms exercise",
    "activity tracking helps improve fitness"
]

query = 'speed walking tracking'

# Combine documents and query
all_texts = docs + [query]

# Compute TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_texts)
tfidf_array = tfidf_matrix.toarray()

# Split into documents and query
doc_vectors = tfidf_array[:3]
query_vector = tfidf_array[3].reshape(1, -1)

# Compute cosine similarity
cos_sim = cosine_similarity(doc_vectors, query_vector).flatten()

# Dimensionality reduction for visualization
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(tfidf_array)

# Plot
plt.figure(figsize=(8,6))
labels = ['D1', 'D2', 'D3', 'Query']
colors = ['blue', 'green', 'red', 'black']
for i, (x, y) in enumerate(reduced_vectors):
    plt.scatter(x, y, color=colors[i], label=labels[i], s = 100)
    plt.text(x+0.01, y+0.01, labels[i], fontsize=12)

plt.title('TF-IDF Vectors in 2D (PCA)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.grid(True)

# Save plot
plt.savefig('tfidf_vectors.png')
plt.close()

# Print cosine similarities
print("Cosine Similarities: ")
for i, sim in enumerate(cos_sim, 1):
    print(f'D{i} vs Query: {sim:.3f}')