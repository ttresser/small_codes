x = input("Digite um número inteiro: ")
j = len(x)
x = int(x)
#xi = x
NaoAdja = True

while j > 1 and NaoAdja:
    x0 = x % 10
    x = x // 10
    x1 = x % 10
    if x1 == x0:
        NaoAdja = False
    j = j - 1
if NaoAdja:
    print("não")
else:
    print("sim")
