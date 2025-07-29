from collections import defaultdict
import re
import pandas as pd

class NGramModelLaplace:
    def __init__(self, n):
        self.n = n
        self.ngram_counts = defaultdict(int) # Count of ngram
        self.context_counts = defaultdict(int) # Count of previous n - 1 words
        self.vocab = set() # Set of all unique vocabulary
    
    # Preprocess the text.
    def preprocess(self, text):
        text = text.lower()
        tokens = re.findall(r'\b\w+\b', text)
        # Add start and end tokens for n > 1
        if self.n > 1:
            tokens = ['<s>'] * (self.n - 1) + tokens + ['</s>']
        return tokens

    # Train the model by counting the ngram and context counts
    def train(self, text):
        tokens = self.preprocess(text)
        self.vocab.update(tokens)
        for i in range(len(tokens) - self.n + 1):
            ngram = tuple(tokens[i:i + self.n])
            context = ngram[:-1]
            self.ngram_counts[ngram] += 1
            self.context_counts[context] += 1
    
    # Add 1 for ngram counts to handle 0 counts [Laplace Smoothing].
    def get_add1_prob(self, ngram):
        context = ngram[:-1]
        count_ngram = self.ngram_counts[ngram]
        count_context = self.context_counts[context]
        V = len(self.vocab)
        prob = (count_ngram + 1) / (count_context + V)
        return prob

    # Generate the probabilities for each ngram and store them in a dataframe
    def generate_all_probs(self):
        results = []
        for ngram in self.ngram_counts:
            prob = self.get_add1_prob(ngram)
            results.append({
                'ngram': ' '.join(ngram),
                'count': self.ngram_counts[ngram],
                'context_count': self.context_counts[ngram[:-1]],
                'probability': round(prob, 4)
            })
        
        return pd.DataFrame(results)

    # Predict next word based on the last n words
    def predict_next_word(self, context_words):
        if len(context_words) != self.n - 1:
            raise ValueError(f'Context must be {self.n - 1} words for an {self.n}-gram model.')
        
        # Make sure that the context words are in the form of tuple
        context = tuple(context_words)
        possible_next_words = {}

        # Find all n-grams that start with the given context
        for ngram in self.ngram_counts:
            if ngram[:-1] == context:
                word = ngram[-1]
                prob = self.get_add1_prob(ngram)
                possible_next_words[word] = prob
        
        # If no n-grams found with the given context, use add-1 smoothing for all vocabulary words
        if not possible_next_words:
            context_count = self.context_counts[context]
            V = len(self.vocab)
            for word in self.vocab:
                prob = 1 / (context_count + V)
                possible_next_words[word] = prob
        
        # Sort the predictions in descending order of their probabilities
        sorted_predictions = sorted(possible_next_words.items(), key=lambda item:item[1], reverse=True)
        return sorted_predictions
    
if __name__ == '__main__':
    text = "She saw a cat. She saw a movie. She saw a movie with a cat."

    # Bigram model
    bigram_model = NGramModelLaplace(2)
    bigram_model.train(text)
    bigram_probs_df = bigram_model.generate_all_probs()

    print("Bigram probabilities with Laplace Smoothing:")
    print(bigram_probs_df)

    # Trigram model
    trigram_model = NGramModelLaplace(3)
    trigram_model.train(text)
    trigram_probs_df = trigram_model.generate_all_probs()

    print("Trigram probabilities with Laplace Smoothing:")
    print(trigram_probs_df)

    # Predict next word using the bigram model
    context_bigram = ('a',)
    predictions_bigram = bigram_model.predict_next_word(context_bigram)
    print(f'\nBigram predictions for context {context_bigram}:')
    for word, prob in predictions_bigram:
        print(f'Word: {word}, Probability: {round(prob, 4)}')
    
    # Predict next word using the trigram model
    context_trigram = ('a', 'movie',)
    predictions_trigram = trigram_model.predict_next_word(context_trigram)
    print(f'\nTrigram predictions for context {context_trigram}:')
    for word, prob in predictions_trigram:
        print(f'Word: {word}, Probability: {round(prob, 4)}')

    
    # @title context_count
    from matplotlib import pyplot as plt
    bigram_probs_df['context_count'].plot(kind='hist', bins=20, title='context_count')
    plt.gca().spines[['top', 'right',]].set_visible(False)
    plt.show()