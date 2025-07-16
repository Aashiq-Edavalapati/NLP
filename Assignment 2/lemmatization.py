from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatize_passage(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in pos_tags]
    lemmatized_sentence = ' '.join(lemmatized_words)
    return [lemmatized_sentence, pos_tags]

# text = "There is nothing either good or bad but thinking makes it so."
text = "The quick brown foxes are jumping over the lazy dogs, but the sleeping cats are not bothered. They had been running yesterday, and they will be running again tomorrow. Better athletes run faster, but even good runners sometimes stumble"
result = lemmatize_passage(text)

print("Original: ", text)
print("Tokenized: ", word_tokenize(text))
print("Pos tag: ", result[1])
print("Lemmatized: ", result[0])