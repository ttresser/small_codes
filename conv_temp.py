print("------- CONVERSOR DE UNIDADES DE TEMPERATURA -------")
n = 0
while n == 0:
    unid1 = input("FROM: [F, C or K?] ") 
    unid2 = input("TO: [F, C or K?] ")
    T1 = input("TEMPERATURE: ")
    if type(T1) != str:
        if (unid1 == 'f') and (unid2 == 'c'):
            T2 = (5 / 9)*(float(T1) - 32)
            n = 1
        elif (unid1 == 'c') and (unid2 == 'f'):
            T2 = (9 / 5)*float(T1) + 32
            n = 1
        elif (unid1 == 'f') and (unid2 == 'k'):
            T2 = (5 / 9)*(float(T1) - 32) + 273
            n = 1
        elif (unid1 == 'k') and (unid2 == 'f'):
            T2 = (9 / 5)*(float(T1) - 273) + 32
            n = 1
        elif (unid1 == 'c') and (unid2 == 'k'):
            T2 = float(T1) + 273
            n = 1
        elif (unid1 == 'k') and (unid2 == 'c'):
            T2 = float(T1) - 273
            n = 1
        elif unid1 == unid2:
            T2 = T1
            n = 1
        else:
            print("Algum argumento invalido!")
    else:
        print("Algum argumento invalido!")
        
print("RESULT: ", T2)
