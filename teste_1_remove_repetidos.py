def repeticoes(vetor0):
    vetor1 = []
    vetor1.append(vetor0[0])
    j = 0; p = 0
    u = len(vetor0)
    while j < u:
        y = vetor1[p]
        if y != vetor0[j]:
            q = vetor0[j]
            vetor1.append(q)
            p = len(vetor1) - 1
        j = j + 1
    return vetor1

def remove_repetidos(lista0):
    lista1 = lista0[:]
    lista2 = []
    lista3 = []
    for a in lista0:
        igual = 0
        for b in lista1:
            if b == a:
                igual = igual + 1
        if igual == 1:
            lista2.append(a)
        else:
            lista3.append(a)
    if len(lista3) > 0:
        lista3.sort()
        lista3 = repeticoes(lista3)
        lista2 = lista2 + lista3
    lista2.sort()
    return lista2
        
def main():
     y = [7, 8, 2, 5, 7, 6, 0, 8, 7, 8, 3, 5, 4, 11, 43]
     w = [3, 7, 12, 33, 3, 100]
     z = [1,2,3]
     print(z)
     print(remove_repetidos(z))

main()
