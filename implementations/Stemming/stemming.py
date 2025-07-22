from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

stemmer = SnowballStemmer("english", True)
text = "There is nothing either good or bad but thinking makes it so."
words = word_tokenize(text)
stemmed_words = [stemmer.stem(word) for word in words]

print("Original:", text)
print("Tokenized: ", words)
print("Stemmed: ", stemmed_words)