#Exemplo 1
'''
vetor = []
for i in range(1,6):
    num = int(input("Digite o número %i de 5:" % i))
    vetor.append(num)
print(vetor)
'''

#Exercício 1
'''
vetor = []
soma = 0
for i in range(1,5):
    notas = int(input("Digite a nota %i: "% i))
    vetor.append(notas)
    soma += notas
for i in range(4):
    print("Nota %i: %i" % (i+1, vetor[i]))

print("Média é ",soma/4 )
'''
#Exercício 2
'''
vetorpar = []
vetorimpar = []

for i in range(1,21):
    num = int(input("Digite o número %i: " % i))
    if num % 2 == 0:
        vetorpar.append(num)
    else:
        vetorimpar.append(num)
print("Pares: ", vetorpar)
print("Impares: ", vetorimpar)
'''

