# 📚 Understanding TF-IDF (Term Frequency-Inverse Document Frequency)

TF-IDF is a numerical statistic used in text mining and natural language processing to measure the importance of a word in a document relative to a collection of documents (corpus). It's widely used for tasks like information retrieval, document similarity, and feature extraction for machine learning models.

---

## 🔍 What is TF-IDF?

TF-IDF combines two metrics:

### 1️⃣ Term Frequency (TF)
Represents how often a word appears in a document.

**Formula:**

$\text{TF}(t) = \frac{\text{Number of times term } t \text{ appears in a document}}{\text{Total terms in the document}}$

### 2️⃣ Inverse Document Frequency (IDF)
Measures how significant a word is across multiple documents.

**Formula:**

$\text{IDF}(t) = \log \left( \frac{\text{Total number of documents}}{\text{Number of documents with term } t} \right)$

Words that appear in many documents (like "the", "is", "and") get lower IDF scores. Rare words get higher scores.

### 🔗 TF-IDF Score

$\text{TF-IDF}(t) = \text{TF}(t) \times \text{IDF}(t)$

This score tells us how important a term is in a particular document while accounting for its overall frequency in the corpus.

---

## 🛠 Implementation Approaches

### 🧠 Manual Calculation
We break down each step:
- Tokenization
- Frequency counting
- TF computation
- IDF computation
- Final TF-IDF aggregation

This helps demystify the math behind the technique.

### ⚙️ Using scikit-learn's `TfidfVectorizer`
A convenient tool that handles preprocessing, stopword removal, and TF-IDF calculation automatically.

---

## 📊 Example

Let’s analyze the relevance of a query using three short documents:

### ✍️ Documents:
- D1: `"Walking is a common activity"`
- D2: `"Running and walking are forms of exercise"`
- D3: `"Activity tracking helps improve fitness"`
- **Query**: `"speed walking tracking"`

After preprocessing (lowercase, stopword removal, tokenization), we get:
- D1: `["walking", "common", "activity"]`
- D2: `["running", "walking", "forms", "exercise"]`
- D3: `["activity", "tracking", "helps", "improve", "fitness"]`
- Query: `["speed", "walking", "tracking"]`

### 📌 Vocabulary (11 unique terms):
`{activity, common, exercise, fitness, forms, helps, improve, running, speed, tracking, walking}`


### 📊 Term Frequency (TF)

Each value represents normalized frequency of a word in a document.

| Term     | D1 (3 terms) | D2 (4 terms) | D3 (5 terms) | Query (3 terms) |
|----------|--------------|--------------|--------------|-----------------|
| activity | 0.333        | 0            | 0.2          | 0               |
| common   | 0.333        | 0            | 0            | 0               |
| exercise | 0            | 0.25         | 0            | 0               |
| fitness  | 0            | 0            | 0.2          | 0               |
| forms    | 0            | 0.25         | 0            | 0               |
| helps    | 0            | 0            | 0.2          | 0               |
| improve  | 0            | 0            | 0.2          | 0               |
| running  | 0            | 0.25         | 0            | 0               |
| speed    | 0            | 0            | 0            | 0.333           |
| tracking | 0            | 0            | 0.2          | 0.333           |
| walking  | 0.333        | 0.25         | 0            | 0.333           |

---

### 🧮 Inverse Document Frequency (IDF)

Calculated across 4 entries: 3 documents + 1 query.

| Term     | Document Count (df) | IDF    |
|----------|---------------------|--------|
| activity | 2                   | 0.693  |
| common   | 1                   | 1.386  |
| exercise | 1                   | 1.386  |
| fitness  | 1                   | 1.386  |
| forms    | 1                   | 1.386  |
| helps    | 1                   | 1.386  |
| improve  | 1                   | 1.386  |
| running  | 1                   | 1.386  |
| speed    | 1                   | 1.386  |
| tracking | 2                   | 0.693  |
| walking  | 3                   | 0.288  |

### 🔢 TF-IDF Vectors (rounded to 3 decimal places):
| Term       | D1     | D2     | D3     | Query  |
|------------|--------|--------|--------|--------|
| activity   | 0.231  | 0      | 0.139  | 0      |
| common     | 0.462  | 0      | 0      | 0      |
| exercise   | 0      | 0.347  | 0      | 0      |
| fitness    | 0      | 0      | 0.277  | 0      |
| forms      | 0      | 0.347  | 0      | 0      |
| helps      | 0      | 0      | 0.277  | 0      |
| improve    | 0      | 0      | 0.277  | 0      |
| running    | 0      | 0.347  | 0      | 0      |
| speed      | 0      | 0      | 0      | 0.462  |
| tracking   | 0      | 0      | 0.139  | 0.231  |
| walking    | 0.096  | 0.072  | 0      | 0.096  |

## 🧮 Cosine Similarity: Measuring Query Relevance

Once we compute the TF-IDF vectors, we use **Cosine Similarity** to measure how closely each document matches the query. The higher the similarity score, the more relevant the document is to the query.

### 📐 Formula:

Given two vectors A and B, their cosine similarity is:

$$\text{CosineSimilarity}(A, B) = \frac{A \cdot B}{|A| \times |B|}$$

Where:

* $(A \cdot B)$ is the dot product of the two vectors.
* $(|A|)$ and $(|B|)$ are the magnitudes (Euclidean norms) of each vector.

### 🔍 Calculation Results:

| Comparison    | Cosine Similarity Score |
| :------------ | :---------------------- |
| D1 vs Query   | 0.034                   |
| D2 vs Query   | 0.022                   |
| D3 vs Query   | **0.118** ✅✅           |

Document **D3 ranks highest** due to overlapping terms like "tracking" and "activity", making it the most relevant to the query "speed walking tracking".


### 📈 Visualization:
TF-IDF vectors are reduced to 2D using PCA and plotted. The query vector is closest to **D3**, confirming its relevance.

---

## 🌟 Why It’s Useful

TF-IDF helps:
- Filter out common, less informative words
- Highlight key terms in documents
- Improve text-based machine learning models by giving meaningful features

---

## 🔗 Further Reading

- [scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Wikipedia – TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

---

📂 This markdown complements the Python code and helps readers grasp the intuition behind TF-IDF. Happy learning!