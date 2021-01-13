#Exemplo 1 com for
'''N = int(input("Digite o valor de N: "))
div = 0
for i in range(1,N+1):
    primo = True
    for j in range(2, i):
        div += 1
        if i % j == 0:
            primo = False
    if primo:
        print(i)
print("Números de divisões: ",div)'''

#Exemplo com while
'''
N = int(input("Digite o valor de N: "))
div = 0
for i in range(1,N+1):
    primo = True
    j = 2
    while j < i and primo:
        div += 1
        if i % j == 0:
            primo = False
        j += 1
    if primo:
        print(i)
print(div)
'''
#Exercício 1
'''
n = int(input("Digite o valor de N: "))
i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))
cont, k = 0, 0
while cont < n:
    if k % i == 0 or k % j == 0:
        print(k)
        cont += 1
    k += 1
'''

#Exercício 2

i = int(input("Digite o valor de i: "))
j = int(input("Digite o valor de j: "))
cont = 1
while cont <= i and cont <= j:
    if i % cont == 0 and j % cont ==0:
        print(cont, end=' ')
    cont += 1
