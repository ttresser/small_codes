def main():
    x = int(input("Digite um número: "))
    lista = []
    while x != 0:
        lista.append(x)
        x = int(input("Digite um número: "))
    for y in range(len(lista) - 1, -1, -1):
        print(lista[y])

main()
        
