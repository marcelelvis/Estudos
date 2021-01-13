#Exemplo 1

import random

meu = [6, 13, 25, 33, 42, 50]

megasena = list(range(1,61))
soma = 0

n = int(input("Número de testes: "))

for i in range(n):
    sorteado = []

    cont = 0


    while meu != sorteado:
        mega_sort = megasena.copy()

        sorteado = []

        for j in range(6):
            num_sorteado = random.choice(mega_sort)
            sorteado.append(num_sorteado)
            mega_sort.remove(num_sorteado)

        sorteado.sort()

        cont += 1
    soma += cont

    print(f"Resultado do teste {i+1}%: {cont}% tentativas")

soma /= n

print(f"Média dos resultados {int(soma)}")