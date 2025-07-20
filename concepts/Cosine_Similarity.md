# 📚 Cosine Similarity

Cosine similarity is a metric used to measure how similar two non-zero vectors are. It calculates the cosine of the angle between two vectors in a multi-dimensional space. The closer the cosine value is to 1, the smaller the angle and the higher the similarity between the vectors. Conversely, a value closer to -1 indicates dissimilarity, and 0 indicates orthogonality (no relationship).

In NLP, vectors often represent documents or sentences (e.g., TF-IDF vectors, Word Embeddings), and cosine similarity is used to determine how semantically related they are.

---

## 🔍 What is Cosine Similarity?

Unlike Euclidean distance, which measures the magnitude of difference between vectors, cosine similarity focuses purely on the **orientation** of the vectors. This makes it particularly useful in high-dimensional spaces, such as those encountered in text analysis, where the magnitude of word counts (or TF-IDF values) can vary significantly between documents.

### Intuition:

* If two vectors point in exactly the same direction (angle = 0 degrees), their cosine similarity is 1. This means they are perfectly similar.
* If two vectors are orthogonal (angle = 90 degrees), their cosine similarity is 0. This means there is no linear relationship or similarity.
* If two vectors point in opposite directions (angle = 180 degrees), their cosine similarity is -1. This means they are perfectly dissimilar.

### Formula:

Given two vectors, A and B, the cosine similarity is calculated as:

$$
\text{Cosine Similarity}(\mathbf{A}, \mathbf{B}) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \, \|\mathbf{B}\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \, \sqrt{\sum_{i=1}^{n} B_i^2}}
$$

Where:
* $A_i$ and $B_i$ are the components of vectors A and B, respectively.
* $A \cdot B$ is the dot product of vectors A and B.
* $\|A\|$ and $\|B\|$ are the Euclidean magnitudes (or L2 norms) of vectors A and B, respectively.

---

## 💡 Example

Let's consider two simple document vectors, represented by their word counts (a very simplified example, but illustrates the concept):

**Document 1 (D1):** "The quick brown fox"
Vector $A = [1, 1, 1, 1, 0, 0]$ (quick, brown, fox, the, lazy, dog)

**Document 2 (D2):** "The quick lazy dog"
Vector $B = [1, 0, 0, 1, 1, 1]$ (quick, brown, fox, the, lazy, dog)

**1. Dot Product ($A \cdot B$):**
$(1 \times 1) + (1 \times 0) + (1 \times 0) + (1 \times 1) + (0 \times 1) + (0 \times 1) = 1 + 0 + 0 + 1 + 0 + 0 = 2$

**2. Magnitude of A ($\|A\|$):**
$\sqrt{1^2 + 1^2 + 1^2 + 1^2 + 0^2 + 0^2} = \sqrt{1 + 1 + 1 + 1 + 0 + 0} = \sqrt{4} = 2$

**3. Magnitude of B ($\|B\|$):**
$\sqrt{1^2 + 0^2 + 0^2 + 1^2 + 1^2 + 1^2} = \sqrt{1 + 0 + 0 + 1 + 1 + 1} = \sqrt{4} = 2$

**4. Cosine Similarity:**
$\frac{2}{2 \times 2} = \frac{2}{4} = 0.5$

A cosine similarity of 0.5 indicates a moderate level of similarity between the two documents.

---

## 🛠 Implementation Approaches

### 🧠 Manual Calculation
We will break down the calculation into its components: dot product and vector magnitudes. This helps solidify the mathematical understanding behind the metric.

### ⚙️ Using `scikit-learn` or `scipy.spatial.distance`
For real-world applications, libraries like `scikit-learn` and `scipy` provide efficient and optimized functions for computing cosine similarity between vectors or matrices of vectors.

---

## 🌟 Why It’s Useful

Cosine similarity is widely used in NLP and other fields for:

* **Document Similarity:** Finding documents that are similar in content (e.g., in search engines, recommender systems).
* **Text Classification:** As a metric to compare a document's vector to class prototypes.
* **Clustering:** Grouping similar documents or words together.
* **Information Retrieval:** Ranking search results based on query similarity.
* **Word Embeddings:** Comparing the semantic similarity of words based on their vector representations (e.g., Word2Vec, GloVe).
* **Question Answering Systems:** Matching user queries to relevant answers.

---

## 🔗 Further Reading

* [Wikipedia – Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
* [scikit-learn Documentation – `cosine_similarity`]([https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html))
* [SciPy Documentation – `scipy.spatial.distance.cosine`]([https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cosine.html))

---

📂 This markdown elaborates on Cosine Similarity, its formula, and its practical applications in NLP.


You can find the implementation details [here](../implementations/)