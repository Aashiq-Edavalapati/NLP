"""
    Exploring TF-IDF (Term Frequency - Inverse Document Frequency) using sklearn's TfidfVectorizer.
    Author: Aashiq
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from nltk.corpus import stopwords

# Sample documents for analysis
documentA = 'The man went out for a walk'
documentB = 'The children sat around the fire'

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