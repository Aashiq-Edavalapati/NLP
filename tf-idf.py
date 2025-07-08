"""
Exploring TF-IDF (Term Frequency - Inverse Document Frequency) using both manual implementation and sklearn's TfidfVectorizer.
Author: Aashiq
"""

import math
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.corpus import stopwords  # Uncomment if you want to filter stopwords

# Sample documents for analysis
documentA = 'the man went out for a walk'
documentB = 'the children sat around the fire'

# Tokenize documents into individual words
bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')

# Create a set of all unique words across both documents
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))

# Initialize word count dictionaries for both documents
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1

numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1

# --- Function to compute Term Frequency ---
def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

# Calculate TF values for each document
tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)

# --- Function to compute Inverse Document Frequency ---
def computeIDF(documents):
    n = len(documents)  # total number of documents
    idfDict = dict.fromkeys(documents[0].keys(), 0)

    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(n / float(val))
    return idfDict

# Compute IDF values across both documents
idfs = computeIDF([numOfWordsA, numOfWordsB])

# --- Function to compute TF-IDF ---
def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

# Manual TF-IDF calculation
tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)

# Display manual TF-IDF scores in DataFrame format
df_manual = pd.DataFrame([tfidfA, tfidfB])
print("Manual TF-IDF values:")
print(df_manual)
print("------" * 20)

# --- Using sklearn's TfidfVectorizer ---
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([documentA, documentB])
feature_names = vectorizer.get_feature_names_out()

# Convert sparse matrix to dense format and display
dense = vectors.todense()
denselist = dense.tolist()
df_sklearn = pd.DataFrame(denselist, columns=feature_names)

print("TF-IDF values using sklearn TfidfVectorizer:")
print(df_sklearn)