def primalidade(n):
    j = 2
    primo = True
    if n == 0 or n == 1:
        primo = False
    else:
        while j < n and primo:
            if (n % j) == 0:
                primo = False
            j = j + 1
    return primo

def n_primos(x):
    i = 0; j = 0
    while i < x:
        primo = primalidade(i)
        if primo:
            j = j + 1
        i = i + 1
    if primalidade(x):
        return(j + 1)
    else:
        return j
