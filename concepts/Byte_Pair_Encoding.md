# 📚 Byte Pair Encoding (BPE)

Byte Pair Encoding (BPE) is a **subword tokenization algorithm** that strikes a balance between character-level and word-level representations. Instead of breaking text into individual characters or full words, BPE learns a vocabulary of common subword units (or "tokens") by iteratively merging the most frequent pairs of characters or character sequences in a training corpus.

It's widely used in modern Natural Language Processing, especially in large language models like GPT, BERT, and T5, because it effectively handles out-of-vocabulary (OOV) words, reduces vocabulary size compared to word-level models, and can represent rare words and new words by combining known subword units.

---

## 🔍 What is Byte Pair Encoding?

The core idea behind BPE is to find the most frequently co-occurring adjacent characters or character sequences and merge them into a new, larger subword unit. This process is repeated until a predefined vocabulary size is reached or no more merges can be made.

### Core Steps:

1.  **Initialize Vocabulary:** Start with a vocabulary of all individual characters present in the training corpus.
2.  **Count Character Pairs:** Count the frequency of all adjacent character pairs in the text.
3.  **Merge Most Frequent Pair:** Identify the most frequent adjacent pair and replace all occurrences of this pair with a new, single subword token.
4.  **Repeat:** Go back to step 2 and repeat the process for a specified number of merge operations or until no more merges are beneficial.

The set of learned merge operations and the final vocabulary of subword units are then used to tokenize new text.

### Example Walkthrough:

Let's illustrate with a simple example:

**Corpus:**
`"low low low lowermost newest"`

**Initial Vocabulary (Characters):** `l, o, w, e, r, m, s, t, n, v` (and space, assuming tokenization first)
Let's represent words as sequences of characters with a special end-of-word token `_`:
`l o w _ l o w _ l o w _ l o w e r m o s t _ n e w e s t _`

**1. Initial Frequencies:**
* `l o`: 4
* `o w`: 4
* `w _`: 3
* ... and so on.

**2. Merge `l o` (most frequent):**
New token: `lo`
Corpus becomes: `lo w _ lo w _ lo w _ lo w e r m o s t _ n e w e s t _`

**3. Merge `lo w` (most frequent now):**
New token: `low`
Corpus becomes: `low _ low _ low _ low e r m o s t _ n e w e s t _`

**4. Merge `_ low` (most frequent):**
New token: `_low` (or just `low` and handle space separately)
Corpus becomes: `low _ low _ low _ low e r m o s t _ n e w e s t _` (if we don't merge across spaces or have spaces as initial tokens, this step might look different depending on implementation details)

Let's simplify and just focus on words:

* **Words:** `low low low lowermost newest`
* **Counts:** `low: 4, lowermost: 1, newest: 1`
* **Initial Characters:** `l o w e r m s t n v`

**Iteration 1:**
* Most frequent pair: `l o` (appears 4 times in `low`)
* Merge `l o` into `lo`
* Corpus now effectively views `low` as `lo w`, `lowermost` as `lo w e r m o s t`

**Iteration 2:**
* Most frequent pair: `lo w` (appears 4 times as `low`)
* Merge `lo w` into `low`
* Corpus words are now effectively tokenized as: `low`, `lowermost` (which is `low` + `ermost`), `newest`

**Iteration 3 (on `newest` and `ermost`):**
* Most frequent pair: `e s` in `newest` (if it's the most frequent globally)
* Merge `e s` into `es`
* Corpus words: `new` `est`, `low` `er` `mo` `st`

This iterative merging process continues, creating subword units like `lo`, `low`, `est`, `new`, `er`, `most`, etc.

### Key Characteristics:

* **Data-Driven:** The subword vocabulary is learned directly from the training data.
* **Out-of-Vocabulary (OOV) Handling:** Any word, no matter how rare or new, can be broken down into known subword units or even individual characters if necessary.
* **Reduced Vocabulary Size:** It results in a vocabulary smaller than a pure word-level vocabulary (which struggles with rare words) but larger than a character-level vocabulary (which loses semantic meaning).

---

## 🛠 Implementation Approaches

A typical BPE implementation involves:

1.  **Preprocessing:** Tokenizing text into words and converting each word into a sequence of characters.
2.  **Frequency Counting:** Counting the occurrences of all character pairs.
3.  **Iterative Merging:** Repeatedly finding and merging the most frequent pair, updating counts, and adding the new merged token to the vocabulary. This continues for a set number of merge operations.
4.  **Encoding/Decoding:** Applying the learned merges to new text to encode it into subword units, and potentially decoding it back.

---

## 🌟 Why It’s Useful

BPE offers significant advantages, especially for modern NLP tasks:

* **Handling OOV Words:** New or rare words can be represented compositionally using existing subword units. For example, "unfriendable" might be broken into "un", "friend", "able".
* **Managing Vocabulary Size:** It creates a manageable vocabulary that captures common patterns while still being able to represent rare words. This is crucial for large language models.
* **Semantic Representation:** Subword units often carry more semantic meaning than individual characters, while being more robust to typos and variations than full words.
* **Language Agnostic:** The algorithm doesn't require linguistic knowledge and can be applied to any language.
* **Efficiency:** It provides an efficient way to represent text for neural networks.

---

## 🔗 Further Reading

* [Neural Machine Translation of Rare Words with Subword Units (Sennrich et al., 2016) - Original BPE paper for NLP](https://arxiv.org/abs/1508.07909)
* [Hugging Face Blog - Byte-Pair Encoding Explained](https://huggingface.co/learn/nlp-course/chapter2/4)
* [Towards Data Science - Demystifying Byte Pair Encoding](https://towardsdatascience.com/byte-pair-encoding-explained-53896564e9a0)
* [Google's SentencePiece (an extension of BPE)](https://github.com/google/sentencepiece)

---

📂 This markdown explains the concept of Byte Pair Encoding, its step-by-step process, key characteristics, and its vital role in modern NLP, particularly in handling large vocabularies and OOV words.

**You can find the implementation [here](../implementations/Byte%20Pair%20Encoding/BPE.py)**