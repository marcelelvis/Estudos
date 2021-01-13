#Exemplo 1
'''
lista = []

num = int(input("Digite um número da sequência: "))

while num != -1:
    lista.append(num)
    num = int(input("Digite um número da sequência: "))

elemento = int(input("Digite o elemento a ser procurado: "))
cont = 0


for i in range(len(lista)): #Usando for
    if lista[i] == elemento:
        cont += 1
                                  #usando for coloca o cont aqui
print(f"O elemento {elemento} aparece {lista.count(elemento)} vezes na sequência.") #Usando count
'''

#Exemplo 2
'''
import random
vetor = []
for i in range(100:)
    vetor.append((random.randint(1,6)))

for i in range(1, 7):
    print(f"A face {i} apareceu {vetor.count(i)} vezes.")
'''

print("Enquete: Quem foi o melhor jogador?")
num = 1
cont = 0
lista = []

while num != 0:
    num = int(input("Informe um valor entre 1 e 23 ou 0 para sair: "))
    if 0 < num <= 23:
        lista.append(num)


print("Resultado da votação:")
print(f"Foram computados {len(lista)} votos.")

