#Exercício 1, invertendo os elementos da lista
'''
idades = []
alturas = []

for i in range(1,6):
    idade = int(input(f"Digite a idade {i} de 5: "))
    altura = float(input(f"Digite a altura(m) da pessoa {i} de 5: "))

    idades.append(idade)
    alturas.append(altura)
'''
'''
#Usando slice
idades_invertida = idades[::-1]
alturas_invertida = alturas[::-1]

for i in range(5):
    print(f"Idade {5-i}: {idades_invertida[i]}")
    print(f"Alutra {5-i}: {alturas_invertida[i]:.2f}")
'''
'''
#Usando range

for i in range(4,-1,-1):
    print(f"Idade {i+1}: {idades[i]}")
    print(f"Altura {i+1}: {alturas[i]}")
'''
'''
#Usando método reverse

idades.reverse()
alturas.reverse()
for i in range(5):
    print(f"Idade {5-i}: {idades[i]}")
    print(f"Alutra {5-i}: {alturas[i]}")
'''
#Mostrando o remove
'''
l1 = [1,2,3]]
l1.remove(2)
print(l1)
'''
'''
#Exemplo jogo
import random

player_vida = 500

play_mana = 100

inimigo_vida = 50

n = int(input("Digite o número de inimigos: "))
inimigos = []

for i in range(n):
    inimigos.append([i+1, inimigo_vida])

jogando = True

while jogando:
    #Imprimimos na tela a vida e a mana
    print(f"Vida: {player_vida}")
    print(f"Mana: {play_mana}")

    atk = int(input("Deseja atacar (1) ou curar (2): "))

    if atk == 1:
        selecionado = random.choice(inimigos)
        dano = random.randint(10, 15)
        print(f"Causou {dano} de dano ao inimigo {selecionado[0]}")
        selecionado[1] -= dano

        if selecionado[1] <= 0:
            print(f"Inimigo {selecionado[0]} morreu!")
            inimigos.remove(selecionado)
    else:
        if play_mana >= 10:
            cura = random.randint(10, 15)
            print(f"Você recebeu {cura} de vida!")
            player_vida += cura
            #Diminui a mana do player
            play_mana -= 10
        else:
            print("Mana insuficiente")
    for inimigo in inimigos:
        #escolhemos se o inimigo vai acertar ou errar
        #O inimigo tem 75% de chance de acertar
        acertou = bool(random.choice([1,1,1,0]))
        if acertou:
            dano = random.randint(1,3)
            print(f"Inimigo {inimigo[0]} causou {dano} de dano!")
            player_vida -= dano
        else:
            print(f"Inimigo {inimigo[0]} errou o ataque!")
    if play_mana < 100:
        play_mana += 3
    if play_mana > 100:
        play_mana = 100
    if player_vida <= 0:
        print("Perdeu o jogo!")
        jogando = False
    if len(inimigos) == 0:
        print("Parabéns você venceu o jogou!")
        jogando = False
'''

#Exercício 1
notas = []
notasreversa = []
valor = int(input("Digite as notas: "))
cont = 0
soma = 0
media = 0
acima = 0
abaixo = 0
while valor != -1:
    notas.append(valor)
    valor = int(input("Digite as notas: "))

print(f"Quantidades de valores lidos {len(notas)}")
print(f"Ordem que foram informados: ", end=' ')
for i in notas:
    print(f'{i:.0f}', end=' ')
notas.reverse()
print("\nOrdem contária: ", end=' ')
for i in notas:
    print('',i, end=' ')
for i in notas:
    soma += i
print(f"\nA soma é: {soma}")
media = soma/len(notas)
print(f"A média é: {media}")
for i in notas:
    if i > media:
        acima += 1
print(F'\nNúmeros de notas acima é {acima}')
for i in notas:
    if i < 7:
        abaixo += 1
print(f'\nNúmeros de notas abaixo de 7 é {abaixo}')
print("\nIsso é tudo pessoal!!")
