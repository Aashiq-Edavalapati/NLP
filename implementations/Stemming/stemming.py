# Import necessary libraries from NLTK
from nltk.stem.snowball import SnowballStemmer     # For stemming words (reducing to root form)
from nltk.tokenize import word_tokenize            # For splitting text into individual tokens

# Initialize the Snowball stemmer for English
# The second parameter 'True' enables ignoring case sensitivity while stemming
stemmer = SnowballStemmer("english", True)

# Sample input text
text = "There is nothing either good or bad but thinking makes it so."

# Tokenize the cleaned text into proper word tokens
words = word_tokenize(text)

# Apply stemming to each token
stemmed_words = [stemmer.stem(word) for word in words]

# Print results
print("Original:", text)
print("Tokenized: ", words)
print("Stemmed: ", stemmed_words)
