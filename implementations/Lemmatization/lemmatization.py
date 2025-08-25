# Importing required libraries from NLTK
from nltk.stem import WordNetLemmatizer      # For lemmatization (reducing words to base form)
from nltk.corpus import wordnet              # WordNet corpus helps with POS tags for lemmatization
from nltk import word_tokenize, pos_tag      # Tokenization (splitting text into words) and POS tagging

# Helper function to convert POS tag from nltk.pos_tag to the format WordNet understands
def get_wordnet_pos(tag):
    """
        Map POS (Part-of-Speech) tags from nltk.pos_tag to WordNet POS tags.
        WordNet requires specific POS tags (NOUN, VERB, ADJ, ADV).
        If the tag is unknown, default to NOUN.
    """
    if tag.startswith('J'):
        return wordnet.ADJ   # Adjective
    elif tag.startswith('V'):
        return wordnet.VERB  # Verb
    elif tag.startswith("N"):
        return wordnet.NOUN  # Noun
    elif tag.startswith("R"):
        return wordnet.ADV   # Adverb
    else:
        return wordnet.NOUN  # Default to noun if nothing matches

# Function to lemmatize a passage
def lemmatize_passage(text):
    """
        Takes a text passage and:
            1. Tokenizes it into words
            2. Finds the POS tags for each word
            3. Lemmatizes each word using its POS tag (for better accuracy than default noun assumption)
            4. Reconstructs a lemmatized sentence
        Returns:
            - lemmatized sentence (string)
            - original POS tags (list of tuples)
    """
    words = word_tokenize(text)  # Step 1: Break text into tokens
    pos_tags = pos_tag(words)    # Step 2: Get POS tags for each token
    
    lemmatizer = WordNetLemmatizer()  # Initialize lemmatizer
    
    # Step 3: Lemmatize each word with its proper POS tag
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
    
    # Step 4: Join the lemmatized words back into a sentence
    lemmatized_sentence = ' '.join(lemmatized_words)
    
    return [lemmatized_sentence, pos_tags]

# Sample text for testing
text = "The quick brown foxes are jumping over the lazy dogs, but the sleeping cats are not bothered. They had been running yesterday, and they will be running again tomorrow. Better athletes run faster, but even good runners sometimes stumble"

# Run the lemmatization pipeline
result = lemmatize_passage(text)

# Print outputs to see each stage clearly
print("Original: ", text)                        # Original input text
print("Tokenized: ", word_tokenize(text))        # Step 1: Tokenized words
print("POS tag: ", result[1])                    # Step 2: POS tagging result
print("Lemmatized: ", result[0])                 # Final lemmatized sentence
