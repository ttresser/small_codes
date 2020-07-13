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

def main():
    x = int(input("Digite um número inteiro positivo maior ou igual a 2: "))
    if x < 2:
        print("Número inválido!")
    else:
        j = 2
        while x > 1:
            multip = 0
            while (x % j) == 0:
                x0 = x
                x = x // j
                print(x0, end = '\t'); print("|", end = '\t'); print(j)
                multip = multip + 1
            if multip != 0:
                print(end = '\t'); print("|", end = '\t'); print(end = '\t')
                print("[ O fator", j, "possui multiplicidade", multip, "]")
                multip = 0
            j = prox_numero_primo(j)
        print(x, end = '\t'); print("|", end = '\t'); print("-")
                
main()
