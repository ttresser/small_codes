import math
num = int(input("Digite um número inteiro: "))
num0 = num
num = int(math.sqrt(num0**2))
soma = 0
while num >= 10:
    x = num % 10
    soma = soma + x
    num = num // 10
soma = soma + num
print(soma)
