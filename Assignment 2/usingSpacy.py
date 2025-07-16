import spacy

sp = spacy.load('en_core_web_sm')
sentence = sp(u'Manchester United is looking to sign a forward for $90 million')

for word in sentence:
    print(word.text, word.pos_)

sentence2 = sp(u"Manchester United isn't looking to sign any forward.")

for word in sentence2:
    print(word.text, word.pos_, word.dep_)

for entity in sentence.ents:
    print(entity.text + ' - ' + entity.label_ + ' - ' + str(spacy.explain(entity.label_)))

for word in sentence2:
    print(word.text, word.lemma_)