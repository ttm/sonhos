# htrc-feature-reader
# nltk # único p wordnet?
# spaCy # faster and restricted version of nltk
# scikit-learn nlp data mining, bag of words
# gensin # topic modeling and document similarity, semantics analysis, LDA
# TextBlob # nltk interface
# Stanford CoreNLP # Multiple Languages
# polyglot # POS tag multilíngua, named entity, transliterate
#          # lang detection, 
# morphological analysis and wicked problems: https://github.com/JohannesBuchner/zwicky-morphological-analysis

from nltk.corpus import wordnet as wn
import nltk as k
from polyglot.transliteration import Transliterator
transliterator = Transliterator(source_lang="en", target_lang="pt")
print(transliterator.transliterate("preprocessing"))

corpora =   open("../corpora/corpora.txt")
corpora2 = open("../corpora/corpora2.txt")
texte=k.corpus.gutenberg.sents("shakespeare-macbeth.txt")
textp=k.corpus.machado.sents("romance/marm08.txt") # dom casmurro

c1 = corpora.readlines()
c2 = corpora2.readlines()

def paras(textline):
    paragraphs = [""]
    parn = 0
    lock = 0
    for line in textline:
        if not line or (line.count(" ")+line.count("\n")) == len(line):
            if not lock:
                lock = 1
                paragraphs.append("")
                parn += 1
        lock = 0
        paragraphs[parn] += line.replace("\n", "")
        if line.count("\n"):
           paragraphs.append("")
           parn += 1
           lock = 1
    return paragraphs

paras1 = paras(c1)
paras2 = paras(c2)

sents_paras1 = [k.tokenize.sent_tokenize(paragraph, language="portuguese")
          for paragraph in paras1] 
sents_paras2 = [k.tokenize.sent_tokenize(paragraph, language="portuguese")
                for paragraph in paras2] 
words_sents_paras1 = [[k.tokenize.word_tokenize(sent) for sent in parag]
        for parag in sents_paras1]
words_sents_paras2 = [[k.tokenize.word_tokenize(sent) for sent in parag]
        for parag in sents_paras2]

words_sents_parase = k.corpus.gutenberg.sents("shakespeare-macbeth.txt")

words_sents_parasp = k.corpus.machado.sents("romance/marm08.txt") # dom casmurro

# acessar o synset de cada palavra
wordp = words_sents_paras2[10][1][1] # 'janelas'
synp = wn.synsets(wordp, lang="por")
synp2 = wn.synsets("janela", lang="por")
syne = wn.synsets("windows")

# O ideal é usar o synset que tem o POS tag igual

# mudar para algum membro de alguma relação
# 
