def retangulo_vazio():
    a = int(input('digite a largura: '))
    b = int(input('digite a altura: '))
    i = 1; j = 1
    while i <= b:
        if i == 1 or i == b:
            while j <= (a - 1):
                print('#', end = '')
                j = j + 1
        else:
            print('#', end = '')
            while j <= (a - 2):
                print(' ', end = '')
                j = j + 1
        print('#')
        i = i + 1; j = 1

retangulo_vazio()
