def maior_elemento(lista):
    y = lista[0]
    for x in lista:
        if x > y:
            y = x
    return y
            
