import random
'''
lista = []
for i in range(19):
    a = (random.randrange(1,327))
    lista.append(a)

for num in lista:
    centenas = num // 100
    dezenas = (num%100)//10
    unidades = num%10

    saida = str(num) + ' = '

    if centenas > 0:
        saida += str(centenas)
        if centenas > 1:
            saida += ' centenas'
        else:
            saida += ' centana'

        if dezenas > 0:
            if unidades > 0:
                saida += ', '
            else:
                saida += ' e '
        else:
            if unidades > 0:
                saida += ' e '
    if dezenas > 0:
        saida += str(dezenas) + ' dezena'
        if dezenas > 1:
            saida += 's'

        if unidades > 0:
            saida += ' e '
    if unidades > 0:
        saida += str(unidades) + ' unidade'
        if unidades > 1:
            saida += 's'

    print(saida)
'''
#Exercício 1
'''
def main():
    impressao = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

    atleta = str(input("Digite o nome do atleta: "))

    saltos = []
    while atleta != '':

        for i in range(len(impressao)):
            salto = float(input(f"{impressao[i]} salto: "))
            (saltos.append(salto))

        print(f'Resultado final:'
              f'\nAtleta: {atleta}')

        impsalto = "Saltos: "
        for i in range(5):
            impsalto += str(saltos[i])
            if i == 4:
                break
            impsalto += ' - '
        print(impsalto)
        print(medias(saltos))
        break

def medias(numeros):
    soma = 0
    for i in numeros:
        soma += i
    return soma / len(numeros)


main()
'''
def main():
    atleta = str(input(f"Atleta: "))
    notas = []
    for i in range(7):
        nota = float(input("Nota: "))
        notas.append(nota)
    maior = 0
    menor = 10
    for num in notas:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    print(f'Resultado final: '
          f'\nAtleta: {atleta}'
          f'\nMelhor nota: {maior}'
          f'\n Pior nota: {menor}'
          f'\nMedia: {media(notas)}')

def media(lista):
    soma = 0
    menor = 10
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
        if i < menor:
            menor = i
        soma += i
    soma = soma - maior - menor
    return soma / 5


main()