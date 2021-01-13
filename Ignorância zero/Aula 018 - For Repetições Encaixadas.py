#Exemplo 1
'''
começo = int(input("Começo = "))
fim = int(input("Fim = "))
for i in  range(começo, fim+1):
    print('')
    print("Para %d:"%i)
    for j in range(começo, fim+1):
        print("%dx%d = %d" %(i,j,i*j))
'''
#Exemplo 2
'''
n = int(input("Digite um numero de sequências: "))

for i in range(n):
    print("Sequência %d: "% (i+1))
    num = int(input("Digite um numero da sequencia: "))
    soma = 0
    while num != 0:
        if num % 2 == 0:
            soma += num
        num = int(input("Digite um número novamente: "))
    print("Soma da sequência é: ", soma)
'''

#Exercícios

