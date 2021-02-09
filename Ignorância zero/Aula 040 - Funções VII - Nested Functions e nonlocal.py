#Exemplo aula
''''
def f1():
    x = 8001
    def f2():
        print(x)
    f2()

f1()
'''
#Exemplo aula 2
'''
def exp(n):
    def eleva(x):
        print(x**n)
    return eleva

f = exp(3)
f(2)
'''
'''
def f1():
    começo = 0
    def f2():
        nonlocal começo
        print(x)
        x += 1

f1()
'''
'''
def lista():
    start = 0
    lista = []
    def incrementa(item):
        nonlocal lista, start
        lista.append(item)
        start += 1
        print(item, start)
    return incrementa

compras1 = lista()
compras1('presunto')
compras1('mortadela')
compras1('queijo')
compras1('pão')
'''

