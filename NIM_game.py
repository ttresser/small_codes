def computador_escolhe_jogada(n, m):
    jogada_decidida = False
    j = m
    while j >= 1 and not jogada_decidida:
        a = n - j
        rest = a % (m + 1)
        if rest == 0:
            jogada_decidida = True
        else:
            j = j - 1
    if jogada_decidida:
        return j
    else:
        if m < n:
            return m
        else:
            return n

def usuario_escolhe_jogada(n, m):
    jogada_decidida = False
    while not jogada_decidida:
        a = int(input("Quantas peças você quer tirar? "))
        if a <= m and a <= n and a >= 1 and n >= m and m >= 1 and n >= 1:
            jogada_decidida = True
        else:
            print("Oops! Jogada inválida! Tente de novo.")
#            print()
#            print("Disgrassa, rapaz! Jogada inválida!")
#            print("Não venhar roubar nessa disgrassa não, na moral!")
#            print("Tente de novo aí, vá!")
#            print()
    return a

def partida():
        n = int(input("Qual será o total de peças do jogo? "))
        m = int(input("Qual será o número limite de peças retiradas por jogada? "))
        print("====================")
        print("O jogo começa com", n, "peças!")
        print("====================")
        rest = n % (m + 1)
        if rest == 0:
            print("VOCÊ COMEÇA, SACANINHA! JOGUE DURO, VÁ!")
            a = usuario_escolhe_jogada(n, m)
            if a == 1:
                print("Você tirou uma peça!")
            else:
                print("Você tirou", a, "peças!")
            b = 'usuario'
        else:
            print("O COMPUTADOR COMEÇA!")
            a = computador_escolhe_jogada(n, m)
            if a == 1:
                print("O Computador tirou uma peça!")
            else:
                print("O Computador tirou", a, "peças!")
            b = 'computador'
        n1 = n - a
        while n1 > 0:
            print("Agora restam", n1, "peças em jogo.")
            print("====================")
            if b == 'usuario':
                a = computador_escolhe_jogada(n1, m)
                if a == 1:
                    print("O Computador tirou uma peça!")
                else:
                    print("O Computador tirou", a, "peças!")
                b = 'computador'
            else:
                a = usuario_escolhe_jogada(n1, m)
                if a == 1:
                    print("Você tirou uma peça!")
                else:
                    print("Você tirou", a, "peças!")
                b = 'usuario'
            n1 = n1 - a
        if b == 'usuario':
            print("Fim de partida!", "Você ganhou!")
        else:
            print("Fim de partida!", "O Computador ganhou!")
        return b
            
def campeonato():
        b = 'quem'
#    continuar = True
#    while continuar:
        print("******** JOGO NIM ********")
        print()
        print("Escolha:")
        print("1 = Para jogar uma partida isolada")
        print("2 = Para jogar um campeonato")
        x = int(input("--> "))
        print("====================")
        if x == 1:
            print("Você escolheu jogar uma partida isolada!")
            partida()
        if x == 2:
            print("Você escolheu jogar um campeonato!")
            j = 1
            pu = pc = 0
            while j <= 3:
                print("====================")
                print("******** RODADA", j, "********")
                partida()
                if b == 'usuario':
                    pu = pu + 1
                else:
                    pc = pc + 1
                j = j + 1
            print("====================")
            print("Placar: Você", pu, "X", pc, "Computador")
            if pu > pc:
                print("**** VOCÊ É O CAMPEÃO! ****")
            else:
                print("**** O COMPUTADOR FOI O CAMPEÃO! ****")
#        print("====================")
#        print("******** Deseja tentar novamente? ********")
#        y = input("Tecle 'S', em caso afirmativo, ou qualquer outra tecla, em caso negativo: ")
#        print()
#        if y == 'S' or y == 's':
#            continuar = True
#        else:
#            continuar = False
#    print("******** ATÉ BREVE! ********")
#    input("Tecle 'Enter' para fechar.")
    
campeonato()
