'''
matriz = []

m = int(input("Digite a linha da matriz: "))
n = int(input("Digite número de colunas: "))

def constroimatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input(f"Digite o elemento {i}{j} da matriz: "))
            linha.append(x)
        matriz.append(linha)
constroimatriz(m,n, matriz)

print(matriz)
'''
'''
matriz = []

m = int(input("Digite a linha da matriz: "))
n = int(input("Digite número de colunas: "))


def constroimatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input(f"Digite o elemento {i}{j} da matriz: "))
            linha.append(x)
        matriz.append(linha)

def Troca(pos1, pos2, matriz):
    elemento1 = matriz[pos1//10][pos1%10]
    elemento2 = matriz[pos2//10][pos2%10]
    matriz[pos1[0]][pos1[1]] = elemento2
    matriz[pos2[0]][pos2[1]] = elemento1

constroimatriz(m, n, matriz)
pos1 = int(input("Digite a posição do elemento 1: "))
pos2 = int(input("Digite a posição do elemento 2: "))
'''
'''
import random
matriz = []
def geraMatriz(matriz):
    lista = list(range(16))
    for j in range(4):
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)
for i in range(3):
    matriz = []
    geraMatriz(matriz)
    print(matriz)
'''
#aula da UFF criar matriz
'''
m = int(input("Digite a linha da matriz: "))
n = int(input("Digite número de colunas: "))

notas = []
for i in range(m):
    linha = []
    for j in range(n):
        msg = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        linha.append(msg)
    notas.append(linha)
for i in range(3):
    print(notas[i])
'''
'''
#Outro exemplo aula UFF
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        msg = int(input(f"Número da célula [{i}][{j}]? "))
        linha.append(msg)
    matriz.append(linha)
pares = 0
for linha in matriz:
    for e in linha:
        if e % 2 == 0:
            pares += 1
for linha in matriz:
    print(linha)
print(f"A matriz contém {pares} números pares")
'''

'''

#UFF, matriz com pessoas nome e idade

pessoas = []
for i in range(3):
    nome = input(f"Nome da pessoa {i+1}? ")
    idade = int(input(f"Idade de {nome}? "))
    pessoas.append([nome, idade])

menor = 0
for i in range(len(pessoas)):
    if pessoas[i][1] < pessoas[menor][1]:
        menor = i
for pessoa in pessoas:
    print(pessoa)
print(f'A pessoa mais nova é {pessoas[menor][0]}') # O zero é p mostrar o nome da pessoa
'''

'''
matriz = []

for i in range(2): #3
    turma = []
    for k in range(3):
        alunos = []
        for j in range(5):#5
            notas = list(range(5))
            alunos.append(notas)
        turma.append(alunos)
    matriz.append(turma)
for i in matriz:
    print(i)
'''
'''
lin = int(input("Informe o número de linhas da matriz: "))
col = int(input("Informe o número de colunas da matriz: "))

matriz = []

for i in range(lin):
    linha = []
    for j in range(col):
        elemento = int(input(f"Digite o elemento {i+1}{j+1} da matriz: "))
        linha.append(elemento)
    matriz.append(linha)

for k in matriz:
    print(k)
'''

