#def main():
print("------- FORMULA DE BHASKARA -------")
print("----- PARA EQUACOES DE GRAU 2 -----")
print("-------- AX^2 + BX + C = 0 --------")
import math
a = float(input("Digite o coeficiente do termo quadratico: "))
b = float(input("Digite o coeficiente do termo linear: "))
c = float(input("Digite o termo independente: "))
def delta(a, b, c):
    delt = b**2 - 4*a*c
    return delt
if a != 0:
    if delta(a , b, c) > 0:
        x1 = (-b + math.sqrt(delta(a, b, c))) / (2*a)
        x2 = (-b - math.sqrt(delta(a, b, c))) / (2*a)
#            print("Essa equacao de grau 2 possui duas raizes reais, a saber:", x1, "e", x2)
        if x1 < x2:
            print("as raízes da equação são", x1, "e", x2)
            input()
        else:
            print("as raízes da equação são", x2, "e", x1)
            input()
    if delta(a, b, c) == 0:
        x = (-b) / (2*a)
#            print("Essa equacao possui apenas uma raiz real, a saber:", x)
        print("a raiz desta equação é", x)
        input()
    if delta(a, b, c) < 0:
            rx = (-b) / (2*a)
            imx = math.sqrt(-delta(a, b, c)) / (2*a)
            print("Essa equacao possui duas raizes complexas, a saber:", rx, "+ j", imx, "e", rx, "- j", imx)
            input()
#        print("esta equação não possui raízes reais")
else:
     print("Essa nao eh uma equacao de grau 2.")
     input()

#main()
