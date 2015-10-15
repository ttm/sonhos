import nltk as k

#ss=k.corpus.wordnet.synset("thumb")
aa=k.corpus.wordnet.synsets("word")
print("hypernyms: ", aa[0].hypernyms(),"\nhyponyms: ", aa[0].hyponyms())
print("\n\nall methods:", dir(aa[0]))

