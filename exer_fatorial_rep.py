def fatorial(num):
    if num > 0:
        fat = num
    if num == 0:
        fat = 1
    while num > 1:
        num = num - 1
        fat = fat * num
    return fat

def main():
    n = int(input("Digite um número inteiro não-negativo: "))
    while n >= 0:
        print("Seu fatorial é:", fatorial(n))
        n = int(input("Digite um número inteiro não-negativo: "))
    print("Número inválido!") 

main()
