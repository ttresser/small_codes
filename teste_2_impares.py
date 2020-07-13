n = int(input("Digite o valor de n: "))
if n == 0:
    print("no odd numbers will be impressed!")
else:
    j = 0
    while j < n:
        nim = 2 * j + 1
        print(nim)
        j = j + 1
