# script to count chars, tokens, paragraphs of the corpus files
import nltk as k

r=open("../corpora/corpora.txt","r")
t=r.readlines()

tt=[]
npars = 0
for line in t:
    if line =="\n":
        pass
    else:
        tt.append(line[:-1])
        npars += 1
ts=" ".join(tt)
nchars = len(ts)
nsents = len(k.tokenize.sent_tokenize(ts))
ntoks = len(k.tokenize.wordpunct_tokenize(ts))



r=open("../corpora/corpora2.txt","r")
t2=r.readlines()

tt2=[]
npars2 = 0
for line in t2:
    if line =="\n":
        pass
    else:
        tt2.append(line[:-1])
        npars2 += 1
ts2=" ".join(tt2)
nchars2 = len(ts2)
nsents2 = len(k.tokenize.sent_tokenize(ts2))
ntoks2 = len(k.tokenize.wordpunct_tokenize(ts2))








