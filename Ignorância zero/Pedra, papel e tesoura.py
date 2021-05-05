from random import randint

ppt = ['Pedra', 'Papel', 'Tesoura']
maquina = randint(0,2)
jogar = True
while jogar:
    pergunta = int(input("""Faça sua escolha: 
[0] Pedra
[1] Papel
[2] Tesoura
"""))
    print("-="*21)
    print(f"Número escolhido foi {ppt[pergunta]}")
    print(f"Número escolhido pela maquina foi {ppt[maquina]}")
    print("-="*21)

    if maquina == 0:
        if pergunta == 0:
            print("Empate")
        elif pergunta == 1:
            print("Você ganhou")
        elif pergunta == 2:
            print("Você perdeu")
        else:
            print("Entrada inválida")

    elif maquina == 1:
        if pergunta == 0:
            print("Você perdeu")
        elif pergunta == 1:
            print("Empate")
        elif pergunta == 2:
            print("Você ganhou")
        else:
            print("Entrada inválida")

    elif maquina == 2:
        if pergunta == 0:
            print("Você ganhou")
        elif pergunta == 1:
            print("Você perdeu")
        elif pergunta == 2:
            print("Empate")
        else:
            print("Entrada inválida")
    jogar = str(input("Você aindar quer jogar?[S]/[N]\n")).lower()
    if jogar == 's':
        jogar = True
    else:
        jogar = False
