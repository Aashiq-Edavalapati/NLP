"""
    Exploring TF-IDF (Term Frequency - Inverse Document Frequency) using manual implementation.
    Author: Aashiq
"""

import math
import pandas as pd
from nltk.corpus import stopwords

# documentA = input('Enter document A: ').lower()
# documentB = input("Enter document B: ").lower()

# Sample documents for analysis
documentA = 'the man went out for a walk'
documentB = 'the children sat around the fire'

# Tokenize documents into individual words
wordsInA = documentA.split(' ')
wordsInB = documentB.split(' ')

bagOfWordsA = []
bagOfWordsB = []

# Remove stopwords
stopWords = set(stopwords.words('english'))
for word in wordsInA:
    if not word in stopWords:
        bagOfWordsA.append(word)

for word in wordsInB:
    if not word in stopWords:
        bagOfWordsB.append(word)

# Tokenize documents into individual words
bagOfWordsA = ' '.join(bagOfWordsA)
bagOfWordsB = ' '.join(bagOfWordsB)

# Create a set of all unique words across both documents
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))

# Initialize word count dictionaries for both documents
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1

numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1

# --- Function to compute Normalized Term Frequency ---
def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

# Calculate Normalized TF values for each document
tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)

# --- Function to compute Inverse Document Frequency ---
def computeIDF(documents):
    n = len(documents)  # total number of documents
    idfDict = dict.fromkeys(documents[0].keys(), 0)

    # Compute DF (Document Frequency)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

    # Compute IDF (Inverse Document Frequency)
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