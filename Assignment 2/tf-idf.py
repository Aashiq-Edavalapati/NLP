from nltk.corpus import stopwords
import math
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documentA = 'the man went out for a walk'
documentB = 'the children sat around the fire'

# Tokenize documents into words
bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')

# Get the unique words from both documents
uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))

# Count word frequency in each document
numOfWordsA = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] += 1

numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1

# Print English stopwords from nltk
print("NLTK Stopwords:", stopwords.words('english'))

# Compute Term Frequency (TF)
def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF(numOfWordsB, bagOfWordsB)

# Compute Inverse Document Frequency (IDF)
def computeIDF(documents):
    n = len(documents)
    idfDict = dict.fromkeys(documents[0].keys(), 0)

    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log(n / float(val))
    
    return idfDict

idfs = computeIDF([numOfWordsA, numOfWordsB])

# Compute TF-IDF
def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

# Using sklearn's TfidfVectorizer for comparison
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([documentA, documentB])
feature_names = vectorizer.get_feature_names_out()
dense = vectors.todense()
denselist = dense.tolist()
df1 = pd.DataFrame(denselist, columns=feature_names)

print("TF-IDF using sklearn:")
print(df1)
print("------" * 20)

# TF-IDF using manual method
tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)
df2 = pd.DataFrame([tfidfA, tfidfB])

print("TF-IDF using manual implementation:")
print(df2)
