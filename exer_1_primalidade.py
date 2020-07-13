n = int(input("Digite um número inteiro: "))
j = 2
primo = True
if n == 0 or n == 1:
    primo = False
else:
    while j < n and primo:
        rest = n % j
        if rest == 0:
            primo = False
        j = j + 1
if primo:
    print("primo")
else:
    print("não primo")
