def main():
    n = int(input("Digite o valor do expoente do binômio: "))
    k = 0
    while k <= n:
        a = binomial(n, k)
        print(a)
        k = k + 1

def fatorial(x):
    if x >= 0:
        if x == 0:
            fat = 1
        else:
            fat = x
            while x > 1:
                x = x - 1
                fat = fat * x
    return fat

def binomial(n, k):
    cnk = fatorial(n) // (fatorial(k) * fatorial(n-k))
    return cnk

main()
