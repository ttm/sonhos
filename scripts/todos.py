from pylatex import Document, Section, Subsection, Subsubsection, Table, Math, TikZ, Axis, \
            Plot, Figure, Package
from pylatex.utils import italic, escape_latex

doc= Document()
#doc.packages.append(Package('geometry', options=['tmargin=1cm',
#                                                     'lmargin=10cm']))

#with doc.create(Section('The simple stuff')):
#        doc.append('Some regular text and some ' + italic('italic text. '))
#
#with doc.create(Section('The fancy stuff')):
#        with doc.create(Subsection('Correct matrix equations')):
#                    doc.append("Baraca")


r=open("../corpora/corpora.txt","r")
t=r.readlines()
tt=[]
for line in t:
    if line =="\n":
        pass
    else:
        tt.append(line[:-1])
ts=" ".join(tt)
E=""
T=""

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
E+="poema_incidencia.txt -> palavras mais significativas por ordem de incidência\n\n"
T+="\n\n"+poema_incidencia

pic="""# sonho, pessoas outro irmão tudo começa sobre lua havia baratas (é) 
# algo menino porta mim lugar roupa enorme vi pernas casa tio
# sabia diz então namorado pé fazer praia almofada vermelha
# sonhei fiquei andar janela cidade piscina onde olhava todos
# noite buraco muita sala aí bem velho espécie olhos sepre
# skate amigo junto conseguia tomada dentro começou
# ensina assim havima lados ovos acordei cara império consegui"""
f=open("../mineracaoDosSonhos/poema_incidencia_curto.txt","w")
f.write(pic)
f.close()
E+="poema_incidencia_curto.txt -> palavras mais significativas por ordem de incidência, versão ditada e menor\n\n"
T+="\n\n"+pic
with doc.create(Section('Incidência')):
    with doc.create(Subsection("Versão completa")):
        with doc.create(Subsubsection('literatura')):
            doc.append(poema_incidencia)
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras mais significativas por ordem de incidência")
    with doc.create(Subsection('Incidência abreviada')):
        with doc.create(Subsubsection('literatura')):
            doc.append(escape_latex(pic))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras mais significativas por ordem de incidência, versão ditada e mais curta")


#wt__.plot()
W=wt__.tokens
W.sort()
f=open("../mineracaoDosSonhos/palavras_ordenadas_repetidas.txt","w")
f.write(" ".join(W))
f.close()
E+="palavras_ordenadas_repetidas.txt -> palavras mais significativas por ordem alfabética e com repeticoes\n\n"
T+="\n\n"+" ".join(W)

W_=list(set(W))
W_.sort()
f=open("../mineracaoDosSonhos/palavras_ordenadas.txt","w")
f.write(" ".join(W_))
f.close()
E+="palavras_ordenadas.txt -> palavras mais significativas por ordem alfabética\n\n"
T+="\n\n"+" ".join(W_)

with doc.create(Section('Ordenação alfabética')):
    with doc.create(Subsection("Ordenação alfabética com repetição de palavras")):
        with doc.create(Subsubsection('literatura')):
            doc.append(" ".join(W))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras mais significativas por ordem alfabética e com repeticoes")
    with doc.create(Subsection("Ordenação alfabética sem repetição de palavras")):
        with doc.create(Subsubsection('literatura')):
            doc.append(" ".join(W_))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras mais significativas por ordem alfabética")

W__=W_[:]
W__.sort(key = lambda s: -len(s))
f=open("../mineracaoDosSonhos/palavras_tamanhos.txt","w")
f.write(" ".join(W__))
f.close()
E+="palavras_tamanhos.txt -> palavras mais significativas por tamanho\n\n"
T+="\n\n"+" ".join(W__)
with doc.create(Section('Ordenação por tamanho')):
    with doc.create(Subsection('literatura')):
        doc.append(" ".join(W__))
    with doc.create(Subsection('explicação')):
            doc.append("palavras mais significativas por tamanho")


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

ee=[i for i in W__ if pvogal(i,"e")]

f=open("../mineracaoDosSonhos/vogalUnica.txt","w")
f.write(" ".join(ee))
f.close()
E+="vogalUnica.txt -> palavras com uma só vogal\n\n"
T+="\n\n"+" ".join(ee)
aa2=[i for i in W__ if pvogal2(i,"a")]
f=open("../mineracaoDosSonhos/vogalA.txt","w")
f.write(" ".join(aa2))
f.close()
ee2=[i for i in W__ if pvogal2(i,"e")]
f=open("../mineracaoDosSonhos/vogalE.txt","w")
f.write(" ".join(ee2))
f.close()
ii2=[i for i in W__ if pvogal2(i,"i")]
f=open("../mineracaoDosSonhos/vogalI.txt","w")
f.write(" ".join(ii2))
f.close()
oo2=[i for i in W__ if pvogal2(i,"o")]
f=open("../mineracaoDosSonhos/vogalO.txt","w")
f.write(" ".join(oo2))
f.close()
uu2=[i for i in W__ if pvogal2(i,"u")]
f=open("../mineracaoDosSonhos/vogalU.txt","w")
f.write(" ".join(uu2))
f.close()
E+="vogalX.txt -> palavras só com a vogal X\n\n"
T+="\n\n"+" ".join(aa2)
T+="\n\n"+" ".join(ee2)
T+="\n\n"+" ".join(ii2)
T+="\n\n"+" ".join(oo2)
T+="\n\n"+" ".join(uu2)
with doc.create(Section('Palavras com uma só vogal')):
    with doc.create(Subsection('Qualquer vogal')):
        with doc.create(Subsubsection('literatura')):
            doc.append(" ".join(ee))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras com uma só dentre as cinco vogais")
    with doc.create(Subsection('A')):
        with doc.create(Subsubsection('literatura')):
            doc.append(escape_latex(" ".join(aa2)))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras com A")
    with doc.create(Subsection('E')):
        with doc.create(Subsubsection('literatura')):
            doc.append(" ".join(ee2))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras com E")
    with doc.create(Subsection('I')):
        with doc.create(Subsubsection('literatura')):
            doc.append(" ".join(ii2))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras com I")
    with doc.create(Subsection('O')):
        with doc.create(Subsubsection('literatura')):
            doc.append(" ".join(oo2))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras com O")
    with doc.create(Subsection('U')):
        with doc.create(Subsubsection('literatura')):
            doc.append(" ".join(uu2))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras com u")

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
E+="palavraSom.txt -> fricativas com ei, plosivas com ieou, plosivas+m com ae\n\n"
psom_=" ".join(psom+
                psom2+
                psom3)
T+="\n\n"+psom_

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
E+="palavraSom_.txt -> fricativas com ei, plosivas com ieou, plosivas+m com ae com repeticoes\n\n"
psom__=" ".join(psom+
                psom2+
                psom3)
T+="\n\n"+psom__ 


### TTM
with doc.create(Section('palavras por sonoridades')):
    with doc.create(Subsection('com repetições')):
        with doc.create(Subsubsection('literatura')):
            doc.append(escape_latex(psom__.replace("\n","\n\n")))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras com uma só dentre as cinco vogais, com repetições")
    with doc.create(Subsection('sem repetições')):
        with doc.create(Subsubsection('literatura')):
            doc.append(escape_latex(psom_))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras com uma só dentre as cinco vogais, sem repetições")

comeco_fim=[[k.tokenize.word_tokenize(i)[0],k.tokenize.word_tokenize(i)[-2]] for i in k.tokenize.sent_tokenize(ts)]
cf=("{}"*len(comeco_fim)).format(*comeco_fim)
f=open("../mineracaoDosSonhos/comecoFim.txt","w")
f.write(cf)
f.close()
E+="comecoFim.txt -> estilosas palavras que começam e terminam sentenças\n\n"
T+="\n\n"+cf

cf_=("{}"*len(comeco_fim)).format(*["{} {}\n".format(*i) for i in comeco_fim])
f=open("../mineracaoDosSonhos/comecoFim_.txt","w")
f.write(cf_)
f.close()
E+="comecoFim_.txt -> simples palavras que começam e terminam frases\n\n"
T+="\n\n"+cf_

with doc.create(Section('palavras no começo e no fim das frases')):
    with doc.create(Subsection('firulado')):
        with doc.create(Subsubsection('literatura')):
            doc.append(cf)
        with doc.create(Subsubsection('explicação')):
            doc.append("estilosas palavras que começam e terminam sentenças")
    with doc.create(Subsection('simples')):
        with doc.create(Subsubsection('literatura')):
            #doc.append(cf_.replace("\n","\\linebreak "))
            doc.append(escape_latex(cf_))
        with doc.create(Subsubsection('explicação')):
            doc.append("palavras em estilo simples que começam e terminam frases")

# t__.collocations()
#meu irmão; meu namorado; uma espécie; uma pessoa; para mim; outro
#rumo; meu tio; nos olhos; sonhei que; tinha feito; estava namorando;
#para outra; uma mulher; uma prima; algo como; uma amiga; uma piscina;
#uma praia; com isso; que não
collocations="""#meu irmão; meu namorado; uma espécie; uma pessoa; para mim; outro
#rumo; meu tio; nos olhos; sonhei que; tinha feito; estava namorando;
#para outra; uma mulher; uma prima; algo como; uma amiga; uma piscina;
#uma praia; com isso; que não"""
cf_=("{}"*len(comeco_fim)).format(*["{} {}\n".format(*i) for i in comeco_fim])
f=open("../mineracaoDosSonhos/collocations.txt","w")
f.write(collocations)
f.close()
E+="collocations.txt -> termos recorrentes nos sonhos\n\n"
T+="\n\n"+collocations

with doc.create(Section('Termos compostos')):
    with doc.create(Subsection('literatura')):
        doc.append(escape_latex(collocations))
    with doc.create(Subsection('explicação')):
            doc.append("termos compostos recorrentes nos sonhos")



E+="_o_o_ oOo _o_o_"
T+="_o_o_ oOo _o_o_"
T+=E

f=open("../mineracaoDosSonhos/_descricaoDaLiteratura.txt","w")
f.write(E)
f.close()

f=open("../mineracaoDosSonhos/TUDO.txt","w")
f.write(T)
f.close()

doc.generate_pdf("../mineracaoDosSonhos/TUDO")
