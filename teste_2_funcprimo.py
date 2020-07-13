def maior_primo(x):
    x = int(x)
    found = False
    while x >= 2 and not found:
        if numero_primo(x):
            found = True
            return x
        else:
            x = x - 1



def numero_primo(n):
    j = 2
    primo = True
    if n == 0 or n == 1:
        primo = False
        return
    else:
        while j < n and primo:
            rest = n % j
            if rest == 0:
                primo = False
            j = j + 1
    return primo
