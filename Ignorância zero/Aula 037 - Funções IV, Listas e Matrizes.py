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
v = [1,2,3,4,5]

def busca2(x):
    i = 0
    valor = 0
    n = len(v)
    v[n+1] = x
    while v[i] != x:
        i += 1
        if i != n + 1:
            valor = i
    print(i)
busca2(4)


'''
def busca(x):
    while x <= v[n]
        n += 1
        if x <= v[n]
            i = 1
            while v[i] < x:
                i += 1
                if v[i] != x
                    busca() = 0
                else:
                    busca() = i
        else:
            busca() = 0
busca(v)
'''