def retangulo_preenchido():
    a = int(input('digite a largura: '))
    b = int(input('digite a altura: '))
    a0 = a; i = 1; j = 1
    while i <= b:
        while j <= (a - 1):
            print('#', end = '')
            a = a - 1
        print('#')
        b = b - 1
        a = a0

retangulo_preenchido()
