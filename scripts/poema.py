
ss=["Andei de bicicleta por um lugar que tinha paisagistas no canto, meio e no fundo trabalhando como construtores. Pessoas chegaram flutuando como que pousando na Terra (como os aviões , com leveza, só que em pé).",
    "Sonhei que estava em uma aula de artes e quem era a professora era uma prima minha e a aula era na escola em que me formei. Estava tensa porque estava “paquerando” um menino que eu já fiquei mas eu estava namorando um outro menino. Depois eu desisti de “paquerar” o menino e fiquei de boa.  Esse menino que eu estava namorando no sonho não é o meu namorado real, era outro amigo meu.",
    "Lavo muitos lençóis tirados de um mesmo colchão com uma pessoa que toca piano. Havia um império regido por um tirano. Nele havia uma almofada que engole tudo. Jogaram algo nela e a almofada começou a pegar fogo. Pessoas também já haviam caído nessa almofada e tinham ficado presas. Comecei a fazer uma bruxaria para libertar tudo o que tinha ficado preso ali. Mas para que tudo se libertasse era preciso que o império se destruísse."]


import nltk as k, string
# Tokeniza
ss_=[k.Text(k.word_tokenize(i)) for i in ss]

# juntar os tres e fazer analise conjunta deles
# resultar 3 poemas
t=" ".join(ss)
t_=k.word_tokenize(t)
t__=k.Text(t_)

# separar t em stopwords e nao stopwords para analise
sw=set(k.corpus.stopwords.words("portuguese"))
pu=string.punctuation
st=[i for i in t_ if i in sw]
wt=[i for i in t_ if (i not in sw) and (i not in pu)]
pt=[i for i in t_ if i in pu]
st__=k.Text(st)
wt__=k.Text(wt)
pt__=k.Text(pt)

#s1_=k.Text(k.word_tokenize(s1))
#s2_=k.Text(k.word_tokenize(s2))
#### wt__.plot() dá poema
# Menino almofada
# Tudo aula
# Império pessoas
# Outro namorando
# Ficado fiquei
# Pensando também
# Artes terra
# Construtores tensa
# Havia bicicleta nessa professora flutuando
# Fundo presas pessoa boa haviam colchão
# Bruxaria libertar nela andei
# Escola formei algo
# Depois sonhei
# Estava lavo "paquerando" lugar é nele lençóis
# Mas jogaram canto fogo comecei prima
# Destruísse tirados desisti paisagens
# Esse engole começou havia real pé
# Fazer ali muitos chegaram
# Meio amigo precisa leveza
# Sonho regido aviões namorado preso caído 
# Porque pegar trabalhando "paquerar"
# Toca piano tirano libertasse



# s1_ não tem collocations
# s2_ tem

mm=[i for s in ss_ for i in s if i.istitle()]
##### vendo estes, o poema:
#m1=[i for i in s1_ if i.istitle()]
#m2=[i for i in s2_ if i.istitle()]
# Andei, Sonhei,
# Pessoas, depois
# Terra estava
# Esse Esse.

# deixa td minúsculo
# lematiza ou radicaliza
s=k.stem.RSLPStemmer()
# bag of words
