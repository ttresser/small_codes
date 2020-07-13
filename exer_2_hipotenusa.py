def analise_primo(n):
    if n >= 2:
        j = n - 1
        primalidade = True
        while j > 1 and primalidade:
            rest = n % j
            if rest == 0:
                primalidade = False
            j = j - 1
    else:
        primalidade = False
    return primalidade

def prox_numero_primo(n1):
    a = n1 + 1
    primo = analise_primo(a)
    while not primo:
        a = a + 1
        primo = analise_primo(a)
    return a

def é_hipotenusa(x):
    confere = False
    i = 0
    while i < x and not confere:
        q = prox_numero_primo(i)
        if (q % 4) == 1:
            if (x % q) == 0:
                confere = True
            else:
                i = q
        else:
            i = q
    return confere

def soma_hipotenusas(y):
    j = 1; soma = 0
    while j <= y:
        ok = é_hipotenusa(j)
        if ok:
            soma = soma + j
        j = j + 1
    return soma
        
