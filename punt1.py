import spacy
nlp = spacy.load('en_core_web_sm')
text = "I was expecting a surplus of cute close-ups but Burton does surprisingly little to win us over He's never been big on treacle but a bit more warmth in this chilly movie which barely follows the outline of the 1941 original would have gone a long way"
text_sentences = nlp(text)
for sentence in text_sentences.sents:
    print(sentence.text,"/n")