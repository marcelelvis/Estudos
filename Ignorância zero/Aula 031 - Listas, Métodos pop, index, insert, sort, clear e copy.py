#Exemplo 1, pop Ele remove o elemento que vc quer e quando tá sem parametro, ele remove o último elemento da lista
'''
a = [1,2,3,4,5]

indice = int(input(f"Digite o índice (de 0 até {len(a)-1}) do elemento a ser removido: "))

print("Elemento: ", a[indice])

b = []
#Para excluir um elemento ele colocou tudo dentro de b, menos o elemento que não queria(indice)
for i in range(len(a)):
    if i != indice:
        b.append(a[i])

a = b
print(a)

#Ele remove o elemento que vc quer e quando tá sem parametro, ele remove o último elemento da lista
print("Elemento: ", a.pop(indice))
print(a)
'''
"""
#Exemplo 2, index
a = [1,2,3,4,5]

x = int(input("Digite o valor de x:"))
 #Usando while
achei = False
i = 0
while not achei and i < len(a):
    if a[i] == x:
        achei = True
        print(f"Elemento  {x} se encontra no indice {i}")
    i += 1
if not achei:
    print(f"{x} não pertence a lista")

#O index diz em qual indice o elemento está 
print(a.index(x))
"""
#Exemplo 3, insert
'''
a = [1,2,3,4]

print(f"Lista ={a}")
pos = int(input("Digite a posição: "))
ele = int(input("Digite o elemento: "))

b = []

for i in range(len(a)):
    if i == pos: #Se i for igual a posição, ele vai adicionar o valor do elemento em b e em seguida vai adicionar o número da ordem certa
        b.append(ele)

    b.append(a[i])
a = b
print(a)

#Faz o de cima, só q mais fácil kkk 
a.insert(pos,ele)
print(a)
'''
'''
#Exemplo 4, sort, organiza elementos da lista em ordem crescente
a = [5,3,1,2,4]

aux = a[:]
b = []

while len(b) != len(a):
    menor = aux[0]
    for ele in aux:
        if ele < menor:
            menor = ele
    b.append(menor)
    aux.remove(menor)
a = b
print(a)

#Usando sort
a.sort()
print(a)
'''
'''
#Exemplo 5, clear, limpa lista, tira todos elementos

a = [1,2,3,4]
a.clear()
print(a)
'''
'''
#Exmplo 6, copy, copia  lista a para b

a = [1,2,3,4]
b = a.copy()
print(b)
'''