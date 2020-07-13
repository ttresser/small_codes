import re

def le_assinatura():
#    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print()
    print("Assinatura do texto-modelo:")
    wal = float(input("Entre com o tamanho medio de palavra: "))
    ttr = float(input("Entre com a relação Type-Token: "))
    hlr = float(input("Entre com a Razão Hapax Legomana: "))
    sal = float(input("Entre com o tamanho médio de sentença: "))
    sac = float(input("Entre com a complexidade média da sentença: "))
    pal = float(input("Entre com o tamanho medio de frase: "))
    print()

    ass_cp = [wal, ttr, hlr, sal, sac, pal]
    return ass_cp

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    print()
    return textos

def separa_sentencas(texto):
#    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
#    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    frases = re.split(r'[,:;]+', sentenca)
    if frases[-1] == " ":
        del frases[-1]
    return frases

def separa_palavras(frase):
#    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
#    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
#    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def tamanho_medio_palavra(texto):
    lista_sentencas = separa_sentencas(texto)
    total_tam_palavras = 0; total_palavras = 0
    for i in lista_sentencas:
        lista_frases = separa_frases(i)
        for j in lista_frases:
            lista_palavras = separa_palavras(j)
            y = len(lista_palavras)
            total_palavras = total_palavras + y
            for k in lista_palavras:
               x = len(k)
               total_tam_palavras = total_tam_palavras + x
    wal0 = (total_tam_palavras) / (total_palavras)
#    a = [total_tam_palavras, total_palavras, wal0]
    return wal0

def relacao_type_token(texto):
    lista_sentencas = separa_sentencas(texto)
    total_palavras = 0
    t_dif_palavras = []
    for i in lista_sentencas:
        lista_frases = separa_frases(i)
        for j in lista_frases:
            lista_palavras = separa_palavras(j)
            y = len(lista_palavras)
            t_dif_palavras = t_dif_palavras +  lista_palavras
            total_palavras = total_palavras + y
    pala_dif = n_palavras_diferentes(t_dif_palavras)
    ttr0 = (pala_dif) / (total_palavras)
    return ttr0

def razao_hapax_legomana(texto):
    lista_sentencas = separa_sentencas(texto)
    total_palavras = 0; total_uni = []
    for i in lista_sentencas:
        lista_frases = separa_frases(i)
        for j in lista_frases:
            lista_palavras = separa_palavras(j)
            y = len(lista_palavras)
            total_uni = total_uni + lista_palavras
            total_palavras = total_palavras + y
    total_pala_uni = n_palavras_unicas(total_uni)
    hlr0 = (total_pala_uni) / (total_palavras)
    return hlr0

def tamanho_medio_sentenca(texto):
    lista_sentencas = separa_sentencas(texto)
    num_sentencas = len(lista_sentencas); tam_total_sentencas = 0
    for j in lista_sentencas:
        tam_sentenca = len(j)
        tam_total_sentencas = tam_total_sentencas + tam_sentenca
    sal0 = (tam_total_sentencas) / (num_sentencas)
    return sal0

def complex_media_sentenca(texto):
    lista_sentencas = separa_sentencas(texto); num_sentencas = len(lista_sentencas)
    total_frases = 0
    for i in lista_sentencas:
        lista_frases = separa_frases(i)
        p = len(lista_frases)
        total_frases = total_frases + p
    sac0 = (total_frases) / (num_sentencas)
    return sac0

def tamanho_medio_frase(texto):
    lista_sentencas = separa_sentencas(texto)
    t_tam_frases = []; tam_f = 0
    for i in lista_sentencas:
        lista_frases = separa_frases(i)
        t_tam_frases = t_tam_frases + lista_frases
        for j in lista_frases:
            p = len(j)
            tam_f = tam_f + p
    total_frases = len(t_tam_frases)
    pal0 = (tam_f) / (total_frases)
    return pal0

def calcula_assinatura(texto):
#    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = tamanho_medio_palavra(texto)
    ttr = relacao_type_token(texto)
    hlr = razao_hapax_legomana(texto)
    sal = tamanho_medio_sentenca(texto)
    sac = complex_media_sentenca(texto)
    pal = tamanho_medio_frase(texto)
    as_t = [wal, ttr, hlr, sal, sac, pal]
    return as_t

def compara_assinatura(as_a, as_b):
#    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for j in range(0,6):
        f = abs(as_a[j] - as_b[j])
        soma = soma + f
    similaridade = soma / 6
    return similaridade

def avalia_textos(textos, ass_cp):
#    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    n_tex = len(textos); lista_s = []
    for w in textos:
        as_w = calcula_assinatura(w)
        s_w = compara_assinatura(as_w, ass_cp)
        lista_s.append(s_w)
    min_s = lista_s[0]; num_t = 1
    for j in range(1, n_tex):
        if lista_s[j] < min_s:
            min_s = lista_s[j]
            num_t = 1 + j
    return num_t

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    num_tex = avalia_textos(textos, ass_cp)
    print("O autor do texto", num_tex, "está, provavelmente, infectado com COH-PIAH.")
    
main()
