'''
#Exemplo aula
def fatorial(n):
    if n==1:
        return n
    return fatorial(n-1) * n


print(fatorial(5))
'''
#Exercício 1
'''
def xatey(x,y):
    if x <= y:
        print(x)
        xatey(x+1,y)


x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
xatey(x,y)
'''
#Exercício 2


'''
def soma(n):
    if n == 0:
        return n
    return soma(n-1) + n

print(soma(5))'''

def soma(x):
    global s
    if x != 0:
        s += x
        x -= 1
        soma(x)
    return s
s = 0
n = int(input('Digite um número: '))
print(f'\nA soma de {n} até zero é {soma(n)}')