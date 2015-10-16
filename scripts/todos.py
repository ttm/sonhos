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

aa=wt__.vocab()
bb=list(aa.items())
bb.sort(key=lambda s: -s[1])
bb_=[i[0] for i in bb]

# ESCREVE BB
poema_incidencia=("{} "*len(bb_)).format(*bb_)
f=open("../mineracaoDosSonhos/poema_incidencia.txt","w")
f.write(poema_incidencia)
f.close()



f=open("../mineracaoDosSonhos/poema_incidencia_curto.txt","w")
f.write("""# sonho, pessoas outro irmão tudo começa sobre lua havia baratas (é) 
# algo menino porta mim lugar roupa enorme vi pernas casa tio
# sabia diz então namorado pé fazer praia almofada vermelha
# sonhei fiquei andar janela cidade piscina onde olhava todos
# noite buraco muita sala aí bem velho espécie olhos sepre
# skate amigo junto conseguia tomada dentro começou
# ensina assim havima lados ovos acordei cara império consegui""")
f.close()










#wt__.plot()

W=wt__.tokens
W.sort()
f=open("../mineracaoDosSonhos/palavras_ordenadas_repetidas.txt","w")
f.write(" ".join(W))
f.close()

W_=list(set(W))
W_.sort()
f=open("../mineracaoDosSonhos/palavras_ordenadas.txt","w")
f.write(" ".join(W_))
f.close()

W__=W_[:]
W__.sort(key = lambda s: -len(s))
f=open("../mineracaoDosSonhos/palavras_tamanhos.txt","w")
f.write(" ".join(W__))
f.close()



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

ee=[i for i in W__ if pvogal(i,"e")][::-1]

f=open("../mineracaoDosSonhos/vogalUnica.txt","w")
f.write(" ".join(ee))
f.close()



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

aa2=[i for i in W__ if pvogal2(i,"a")][::-1]
f=open("../mineracaoDosSonhos/vogalA.txt","w")
f.write(" ".join(aa2))
f.close()
ee2=[i for i in W__ if pvogal2(i,"e")][::-1]
f=open("../mineracaoDosSonhos/vogalE.txt","w")
f.write(" ".join(ee2))
f.close()
ii2=[i for i in W__ if pvogal2(i,"i")][::-1]
f=open("../mineracaoDosSonhos/vogalI.txt","w")
f.write(" ".join(ii2))
f.close()
oo2=[i for i in W__ if pvogal2(i,"o")][::-1]
f=open("../mineracaoDosSonhos/vogalO.txt","w")
f.write(" ".join(oo2))
f.close()
uu2=[i for i in W__ if pvogal2(i,"u")][::-1]
f=open("../mineracaoDosSonhos/vogalU.txt","w")
f.write(" ".join(uu2))
f.close()

# conjunto de consoantes e vogais
# (d,j,z,h,s,e,i)

def pLetras(palavra,letras):
    if len(palavra)==sum([i in letras for i in palavra]):
        return palavra
    else:
        return 0

# fricativos
psom=[i for i in W__ if pLetras(i,set(["d","j","z","h","s","f","z","j","r","v","e","é","ê","i","í"]))]
# plosivos com eiou
psom2=[i for i in W__ if pLetras(i,set(["d","p","t","q","u","e","é","ê","i","í","o","ó","u","ú","ô"]))]
# plosivos+m com ae
psom3=[i for i in W__ if pLetras(i,set(["d","p","t","q","b","k","c","g","m","x","a","á","ã","â","e"]))]

psom[-1]+="\n"
psom2[-1]+="\n"
f=open("../mineracaoDosSonhos/palavraSom.txt","w")
f.write(" ".join(psom+
                psom2+
                psom3))
f.close()

# fricativos
psom=[i for i in W if pLetras(i,set(["d","j","z","h","s","f","z","j","r","v","e","é","ê","i","í"]))]
# plosivos com eiou
psom2=[i for i in W if pLetras(i,set(["d","p","t","q","u","e","é","ê","i","í","o","ó","u","ú","ô"]))]
# plosivos+m com ae
psom3=[i for i in W if pLetras(i,set(["d","p","t","q","b","k","c","g","m","x","a","á","ã","â","e"]))]

psom[-1]+="\n"
psom2[-1]+="\n"
f=open("../mineracaoDosSonhos/palavraSom_.txt","w")
f.write(" ".join(psom+psom2+psom3))
f.close()

comeco_fim=[[k.tokenize.word_tokenize(i)[0],k.tokenize.word_tokenize(i)[-2]] for i in k.tokenize.sent_tokenize(ts)]
cf=("{}"*len(comeco_fim)).format(*comeco_fim)
f=open("../mineracaoDosSonhos/comecoFim.txt","w")
f.write(cf)
f.close()

cf_=("{}"*len(comeco_fim)).format(*["{} {}\n".format(*i) for i in comeco_fim])
f=open("../mineracaoDosSonhos/comecoFim_.txt","w")
f.write(cf_)
f.close()



#meu irmão; meu namorado; uma espécie; uma pessoa; para mim; outro
#rumo; meu tio; nos olhos; sonhei que; tinha feito; estava namorando;
#para outra; uma mulher; uma prima; algo como; uma amiga; uma piscina;
#uma praia; com isso; que não

cf_=("{}"*len(comeco_fim)).format(*["{} {}\n".format(*i) for i in comeco_fim])
f=open("../mineracaoDosSonhos/colocations.txt","w")
f.write("""#meu irmão; meu namorado; uma espécie; uma pessoa; para mim; outro
#rumo; meu tio; nos olhos; sonhei que; tinha feito; estava namorando;
#para outra; uma mulher; uma prima; algo como; uma amiga; uma piscina;
#uma praia; com isso; que não""")
f.close()

