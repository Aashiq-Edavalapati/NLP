import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

# Documents and query
docs = [
    "Walking is a common activity",
    "Running and walking are forms of exercise",
    "Activity tracking helps improve fitness"
]
query = "Speed walking tracking"

# Combine docs and query for TF-IDF computation
all_texts = docs + [query]
N = len(all_texts)

# Step 1: Preprocessing (lower case, remove stopwords, tokenization)

# 1. Lower case
for i in range(N):
    all_texts[i] = all_texts[i].lower()

# 2. Remove stopwords
stopWords = set(stopwords.words('english'))
for i, doc in enumerate(all_texts):
    words = doc.split()
    newDoc = []
    for word in words:
        if word not in stopWords:
            newDoc.append(word)
    
    all_texts[i] = ' '.join(newDoc)

# 3. Tokenization
vectorizer = TfidfVectorizer()

# Step 2: Compute TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(all_texts)
tfidf_array = tfidf_matrix.toarray()

# Split into documents and query
doc_vectors = tfidf_array[:3]
query_vector = tfidf_array[3].reshape(1, -1)

# Step 3: Compute cosine similarity between each doc and query
cos_sim = cosine_similarity(doc_vectors, query_vector).flatten()

# Dimensionality reduction for visualization using PCA
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(tfidf_array)

# Plot
plt.figure(figsize=(8,6))
labels =['D1', 'D2', 'D3', 'Query']
colors = ['blue', 'green', 'red', 'black']
for i, (x, y) in enumerate(reduced_vectors):
    plt.scatter(x, y, color=colors[i], label=labels[i], s=100)
    plt.text(x + 0.01, y + 0.01, labels[i], fontsize=12)

plt.title('TF-IDF Vectors in 2D(PCA)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.grid(True)
plt.show()

print("Cosine Similarities:")
for i, sim in enumerate(cos_sim, 1):
    print(f'D{i} vs Query: {sim:.3f}')