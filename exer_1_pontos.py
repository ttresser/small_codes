import math
x0 = float(input("Coordenada x do 1o ponto: "))
y0 = float(input("Coordenada y do 1o ponto: "))
xf = float(input("Coordenada x do 2o ponto: "))
yf = float(input("Coordenada y do 2o ponto: "))
d = math.sqrt((xf - x0)**2 + (yf - y0)**2)
if d >= 10:
    print("longe")
else:
    print("perto")
