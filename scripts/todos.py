r=open("../corpora/corpora.txt","r")
t=r.readlines()
tt=[]
for line in t:
    if line =="\n":
        pass
    else:
        tt.append(line[:-1])
ts=" ".join(tt)

import nltk as k, string
# Tokeniza
#ss_=[k.Text(k.word_tokenize(i)) for i in ss]
#
## juntar os tres e fazer analise conjunta deles
## resultar 3 poemas
#t=" ".join(ss)
#t_=k.word_tokenize(t)
#t__=k.Text(t_)
t_=k.word_tokenize(ts)
t_=[i.lower() for i in t_]
t__=k.Text(t_)

# separar t em stopwords e nao stopwords para analise
sw=set(k.corpus.stopwords.words("portuguese"))
pu=string.punctuation
st=[i for i in t_ if i in sw]
pt=[i for i in t_ if i in pu]
wt=[i for i in t_ if (i not in sw) and (i not in pu)]
st__=k.Text(st)
wt__=k.Text(wt)
pt__=k.Text(pt)

#wt__.plot()

W=wt__.tokens
W.sort()
W_=list(set(W))
W_.sort()
W__=W_[:]
W__.sort(key = lambda s: len(s))

def pvogal(palavra,vogal):
    va=["a","á","â","à","ã"]
    ve=["e","é","ê"]
    vi=["i","í"]
    vo=["o","ó","ô","õ"]
    vu=["u","ú","û"]
    todas_vogais=va+ve+vi+vo+vu
    tipo=0
    for letra in palavra:
        if letra in todas_vogais:
            if letra in va:
                tipo_=va
            if letra in ve:
                tipo_=ve
            if letra in vi:
                tipo_=vi
            if letra in vo:
                tipo_=vo
            if letra in vu:
                tipo_=vu
            if tipo==0:
                tipo=tipo_
            else:
                if tipo==tipo_:
                    pass
                else:
                    return 0
    return palavra

ee=[i for i in W__ if pvogal(i,"e")]


def pvogal2(palavra,vogal):
    va=["a","á","â","à","ã"]
    if vogal in va:
        todas_vogais=va
    ve=["e","é","ê"]
    if vogal in ve:
        todas_vogais=ve
    vi=["i","í"]
    if vogal in vi:
        todas_vogais=vi
    vo=["o","ó","ô","õ"]
    if vogal in vo:
        todas_vogais=vo
    vu=["u","ú","û"]
    if vogal in vu:
        todas_vogais=vu
    todas_vogais=set(todas_vogais)
    todas_vogais_=set(va+ve+vi+vo+vu)
    tipo=0
    for letra in palavra:
        if letra in todas_vogais:
            if letra in va:
                tipo_=va
            if letra in ve:
                tipo_=ve
            if letra in vi:
                tipo_=vi
            if letra in vo:
                tipo_=vo
            if letra in vu:
                tipo_=vu
            if tipo==0:
                tipo=tipo_
            else:
                if tipo==tipo_:
                    foo="bar"
                else:
                    return 0
        elif letra in todas_vogais_-todas_vogais:
            return 0
    return palavra

ee2=[i for i in W__ if pvogal2(i,"e")]
ii2=[i for i in W__ if pvogal2(i,"i")]
aa2=[i for i in W__ if pvogal2(i,"a")]
oo2=[i for i in W__ if pvogal2(i,"o")]
uu2=[i for i in W__ if pvogal2(i,"u")]

# conjunto de consoantes e vogais
# (d,j,z,h,s,e,i)

def pLetras(palavra,letras):
    if len(palavra)==sum([i in letras for i in palavra]):
        return palavra
    else:
        return 0

psom=[i for i in W__ if pLetras(i,set(["d","j","z","h","s","e","i"]))]
psom2=[i for i in W__ if pLetras(i,set(["d","p","t","q","u","e","i","o","u"]))]
psom3=[i for i in W__ if pLetras(i,set(["d","p","t","q","b","k","c","g","m","z","x","a","e"]))]











