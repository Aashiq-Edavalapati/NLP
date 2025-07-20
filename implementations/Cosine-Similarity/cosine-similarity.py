"""
    Program to measure the similarity between two sentences using cosine similarity.
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# X = input("Enter the first string: ").lower()
# Y = input("Enter the second string: ").lower()

X = "i love horror movies"
Y = "lights out is a horror movie"

# tokenization
X_list = word_tokenize(X)
Y_list = word_tokenize(Y)

# List of stopwords
sw = stopwords.words('english')
l1 = []
l2 = []

# Remove stop words from the string
X_set = {w for w in X_list if not w in sw}
Y_set = {w for w in Y_list if not w in sw}

# Form a set containing keywords of both strings
rvector = X_set.union(Y_set)
for w in rvector:
    if w in X_set: l1.append(1) # Create a vector
    else: l1.append(0)
    if w in Y_set: l2.append(1)
    else: l2.append(0)

c = 0

# Cosine formula
for i in range(len(rvector)):
    c += l1[i] * l2[i]

cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
print("Similarity: ", cosine)
