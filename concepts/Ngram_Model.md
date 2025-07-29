# 📚 N-gram Language Models

An N-gram model is a type of probabilistic language model that predicts the next item in a sequence (e.g., a word in a sentence) based on the preceding $N-1$ items. It's a fundamental concept in Natural Language Processing (NLP) used for tasks like speech recognition, machine translation, spell checking, and text generation.

---

## 🔍 What is an N-gram?

An N-gram is a contiguous sequence of $N$ items from a given sample of text or speech. The "items" are typically words, but they could also be characters, phonemes, or syllables.

Common types of N-grams include:

* **Unigram ($N=1$):** A single word. (e.g., "the", "cat", "runs")
* **Bigram ($N=2$):** A sequence of two words. (e.g., "the cat", "runs fast")
* **Trigram ($N=3$):** A sequence of three words. (e.g., "the cat runs", "runs fast away")
* And so on (Quadgram, Pentagram, etc.).

---

## 💡 How N-gram Models Work

N-gram models operate on the principle of the **Markov assumption**: the probability of the next word depends only on the previous $N-1$ words, not on all preceding words in the entire history.

### The Core Idea: Predicting the Next Word

The probability of a sequence of words $P(w_1, w_2, ..., w_m)$ can be factored using the chain rule of probability:

$P(w_1, ..., w_m) = P(w_1) P(w_2|w_1) P(w_3|w_1, w_2) ... P(w_m|w_1, ..., w_{m-1})$

Applying the Markov assumption, the conditional probability $P(w_i | w_1, ..., w_{i-1})$ is approximated by $P(w_i | w_{i-(N-1)}, ..., w_{i-1})$.

So, for an N-gram model, the probability of a word $w_i$ given its preceding $N-1$ words (its context) is calculated as:

$$
P(w_i \mid w_{i-(N-1)}, \ldots, w_{i-1}) =
\frac{\text{Count}(w_{i-(N-1)}, \ldots, w_{i-1}, w_i)}
     {\text{Count}(w_{i-(N-1)}, \ldots, w_{i-1})}
$$



Where:
* $\text{Count}(X)$ is the number of times the sequence $X$ appears in the training corpus.
* The numerator is the count of the full N-gram.
* The denominator is the count of the $(N-1)$-gram (the context).

### Training an N-gram Model:

1.  **Tokenization:** The training text is split into words (tokens).
2.  **Add Boundary Tags:** For $N > 1$, special start (`<s>`) and end (`</s>`) tokens are often added to sentences. This helps in modeling sentence beginnings and endings. For an N-gram model, `N-1` start tokens are typically added.
3.  **Count N-grams:** The model counts the occurrences of all N-grams and their corresponding $(N-1)$-gram contexts in the training corpus.

---

## 📉 The Problem of Zero Probabilities: Smoothing

A major challenge with N-gram models is the **zero-frequency problem**. If a particular N-gram (or its context) was not observed in the training data, its count will be zero. This leads to:

* A probability of 0 for any N-gram not seen, which is problematic because even unseen sequences can occur in real language.
* Division by zero if a context itself has a zero count (though less common with start tokens).

To address this, **smoothing techniques** are used to assign a small, non-zero probability to unseen N-grams.

### Laplace Smoothing (Add-1 Smoothing):

Laplace smoothing is one of the simplest and most common smoothing techniques. It adds 1 to all N-gram counts and adds the size of the vocabulary ($V$) to the denominator (the context count).

$$
P_{\text{Laplace}}(w_i \mid w_{i-(N-1)}, \ldots, w_{i-1}) = 
\frac{\text{Count}(w_{i-(N-1)}, \ldots, w_{i-1}, w_i) + 1}
     {\text{Count}(w_{i-(N-1)}, \ldots, w_{i-1}) + V}
$$


Where:
* $V$ is the total number of unique words in the vocabulary (including start/end tokens).

This ensures that no probability is ever zero, though it tends to "over-smooth" and underestimate the probabilities of frequently occurring N-grams.

---

## 🛠 Implementation Details

A typical implementation involves:

* `preprocess(text)`: Converts text to lowercase, tokenizes, and adds start/end tokens as needed.
* `train(text)`: Iterates through the tokens to build `ngram_counts` (frequency of N-grams) and `context_counts` (frequency of the preceding N-1 words). It also builds the `vocab` set.
* `get_add1_prob(ngram)`: Calculates the smoothed probability for a given N-gram using the Laplace (Add-1) smoothing formula.
* `generate_all_probs()`: Computes and displays the probabilities for all observed N-grams in a structured format (e.g., a Pandas DataFrame).
* `predict_next_word(context_words)`: Given a sequence of $N-1$ context words, it predicts the most probable next words by iterating through the vocabulary and calculating smoothed probabilities.

**[Link to N-gram Model Implementation: `implementations/ngram_model_laplace_implementation.py`](../implementations/N%20gram/ngram.py)**

---

## 🌟 Why It’s Useful

N-gram models, despite their simplicity, are widely used as baselines and in various NLP applications:

* **Speech Recognition:** To choose the most likely word sequence given an acoustic input.
* **Machine Translation:** To evaluate the fluency and likelihood of generated translations.
* **Spell Checking and Autocorrect:** To suggest corrections based on common word sequences.
* **Text Generation:** To generate new text by sampling words based on predicted probabilities.
* **Information Retrieval:** Can be used in ranking algorithms.

---

## 🔗 Further Reading

* [Stanford NLP - N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf) (Chapter 3 of Jurafsky & Martin's Speech and Language Processing)
* [Wikipedia – N-gram](https://en.wikipedia.org/wiki/N-gram)
* [Towards Data Science - N-gram Language Models explained with Python](https://towardsdatascience.com/n-gram-language-models-explained-with-python-code-c49b1a533d)

---

📂 This markdown explains the concept of N-gram Language Models, their working principles, the zero-frequency problem and Laplace smoothing, and their common applications in NLP.