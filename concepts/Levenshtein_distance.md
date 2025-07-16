# Levenshtein Distance (Edit Distance)

The **Levenshtein distance**, also known as **Edit Distance**, is a metric for measuring the difference between two sequences (e.g., strings). It quantifies the **minimum number of single-character edits** (insertions, deletions, or substitutions) required to change one word into the other.

It’s a fundamental concept in areas like **spell checking**, **natural language processing (NLP)**, **bioinformatics** (for DNA sequence alignment), and **plagiarism detection**.

---

## 🔍 What is Levenshtein Distance?

Imagine you have two words: `"kitten"` and `"sitting"`.  
How many operations do you need to transform `"kitten"` into `"sitting"`?

### Example:

1. **k**itten → **s**itten *(substitution of 'k' with 's')*
2. sitt**e**n → sitt**i**n *(substitution of 'e' with 'i')*
3. sittin → sitting *(insertion of 'g' at the end)*

✅ **Levenshtein distance = 3**

---

## ✏️ Allowed Edit Operations

1. **Insertion** – Adding a character  
   → Example: `"cat"` → `"cats"`

2. **Deletion** – Removing a character  
   → Example: `"cats"` → `"cat"`

3. **Substitution** – Replacing one character with another  
   → Example: `"cat"` → `"cot"`

---

## 💡 How Is It Calculated? (Dynamic Programming Concept)

The most efficient method to calculate Levenshtein distance is using a **dynamic programming matrix**. Each cell in the matrix represents the distance between two substrings of the original strings.

Let:

- `s1` be the source string of length `m`
- `s2` be the target string of length `n`
- `d(i, j)` be the edit distance between the first `i` characters of `s1` and the first `j` characters of `s2`

### Base Cases:
- `d(i, 0) = i` → i deletions
- `d(0, j) = j` → j insertions

### Recursive Case:
For `i > 0` and `j > 0`,

- If `s1[i-1] == s2[j-1]`,  
  → `d(i, j) = d(i-1, j-1)` *(no operation needed)*

- Else,  
  →  
```

d(i, j) = 1 + min(
d(i-1, j),    # Deletion
d(i, j-1),    # Insertion
d(i-1, j-1)   # Substitution
)

```

The final answer is in `d(m, n)`, the bottom-right cell of the matrix.

---

## 📊 Example: `"saturday"` → `"sunday"`

|       |   | s | u | n | d | a | y |
|-------|---|---|---|---|---|---|---|
| **\_** | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| **s**  | 1 | 0 | 1 | 2 | 3 | 4 | 5 |
| **a**  | 2 | 1 | 1 | 2 | 3 | 4 | 5 |
| **t**  | 3 | 2 | 2 | 2 | 3 | 4 | 5 |
| **u**  | 4 | 3 | 2 | 2 | 3 | 4 | 5 |
| **r**  | 5 | 4 | 3 | 3 | 3 | 4 | 5 |
| **d**  | 6 | 5 | 4 | 4 | 3 | 4 | 5 |
| **a**  | 7 | 6 | 5 | 5 | 4 | 3 | 4 |
| **y**  | 8 | 7 | 6 | 6 | 5 | 4 | 3 |

✅ **Levenshtein distance = 3**

---

## 🌍 Real-World Applications

- 🔤 **Spell Checkers**: Suggesting corrections for typos
- 🔍 **Approximate String Matching**: For fuzzy searches and suggestions
- 📚 **Plagiarism Detection**: Comparing document similarity
- 🧬 **Bioinformatics**: DNA sequence alignment
- 🤖 **NLP Tasks**: Text normalization, machine translation, etc.

---

## 🔗 Further Reading

- [Wikipedia – Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [GeeksforGeeks – Edit Distance Theory](https://www.geeksforgeeks.org/levenshtein-distance-dp-5/)
- [Edit Distance in NLTK Docs](https://www.nltk.org/_modules/nltk/metrics/distance.html)

---

📂 This markdown explains the **theory and applications** of Levenshtein Distance, giving you a strong foundation to implement or use it in real-world projects.
