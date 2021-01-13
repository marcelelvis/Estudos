#Exemplo 1
'''
alunos = 10

medias = []

for i in range(1,alunos+1):
    notas = 0
    for j in range(1, 5):
        notas += float(input(f"Digite a nota {j} de 4 alunos {i} de {alunos}: "))
    notas /= 4
    medias.append(notas)

num = 0

for media in medias:
    if media >= 7.0:
        num += 1

print(f"O número de launos com média maior do que 7 é {num}")
'''
#Exercício 1
'''
lista = []

num = int(input("Digite um número: "))

while num != -1:    
    lista.append(num)
    num = int(input("Digite um número: "))

for i in lista:
    if i > 10:
print(i)
'''

#Exercício 2
'''
lista = []

num = int(input("Digite um número: "))

while num != -1:
    lista.append(num)
    num = int(input("Digite um número: "))
for i in lista:
    if i % 2 == 0:
        print(i)
'''
