#exemplo 1
'''
def soma (*lista):     #Quando coloca Asterísticos, diz que todo numero q vier sera uma tupla, ou seja varios argumentos
    soma_num = 0

    for num in lista:
        soma_num += num

    return soma_num

a = (1,2,3,4)

print(soma(1,2,3,4,5))
'''
"""
#Exemplo 2, peso de provas
def sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

def media (p1,p2,p3, peso1 = 1, peso2 = 1, peso3 = 1):
    return (p1*peso1 + p2*peso2 + p3*peso3)/sum(peso1,peso2,peso3)

print(media(5,5,5))
"""
"""
#Exercício 1
def maior(*mult):
    prod = 1
    for num in mult:
        prod*= num

    return prod

print(maior(4))
"""

def maior(*num):
    num_maior = num[0]
    for i in num:
        if i > num_maior:
            num_maior = i
    return num_maior

print(maior(1,4,70,6,68))