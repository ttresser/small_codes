def maximo(a , b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a >= b and a >= c:
        return a
    else:
        if b >= a and b >= c:
            return b
        else:
            return c
