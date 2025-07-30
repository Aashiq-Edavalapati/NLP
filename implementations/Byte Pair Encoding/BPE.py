from collections import defaultdict

class BytePairEncoding:
    def __init__(self, corpus, num_merges=10):
        self.corpus = corpus
        self.num_merges = num_merges
        self.vocab = self._build_vocab()
    
    def _build_vocab(self):
        vocab = {}
        for word in self.corpus:
            tokens = tuple(word) + ('</w>',)
            vocab[tokens] = vocab.get(tokens, 0) + 1
        return vocab

    def _get_stats(self):
        pairs = defaultdict(int)
        for word, freq in self.vocab.items():
            for i in range(len(word) - 1):
                pairs[(word[i], word[i + 1])] += freq
        return pairs

    def _merge_pair(self, pair):
        new_vocab = {}
        bigram = ' '.join(pair)
        replacement = ''.join(pair)
        for word, freq in self.vocab.items():
            word_str = ' '.join(word)
            new_word_list = []
            i = 0
            while i < len(word_str):
                if word_str[i:].startswith(bigram):
                    new_word_list.append(replacement)
                    i += len(bigram)
                else:
                    new_word_list.append(word_str[i])
                    i += 1
            new_vocab[tuple(''.join(new_word_list).split())] = freq
        self.vocab = new_vocab
    
    def train(self):
        print("Initial Vocabulary:")
        self._print_vocab()

        for i in range(self.num_merges):
            pairs = self._get_stats()
            if not pairs:
                break
                
            best_pair = max(pairs, key=pairs.get)
            print(f'\nMerge {i + 1}: {best_pair}')
            self._merge_pair(best_pair)
            self._print_vocab()
    
    def _print_vocab(self):
        for word, freq in self.vocab.items():
            print(f'{''.join(word)}: {freq}')
    
    def get_vocab(self):
        return self.vocab

    def get_bpe_tokens(self):
        """
            Returns a flat set of learned BPE tokens/subwords.
            Each token is a string.
        """
        token_set = set()
        for word in self.vocab:
            token_set.update(word)
        return sorted(token_set)

if __name__ == '__main__':
    # Train BPE
    bpe = BytePairEncoding(["low", 'lowest', 'newer', 'wider'], 15)
    bpe.train()

    # Display final BPE subword vocabulary
    bpe_tokens = bpe.get_bpe_tokens()
    print('\nFinal BPE Vocabulary: ')
    print(bpe_tokens)