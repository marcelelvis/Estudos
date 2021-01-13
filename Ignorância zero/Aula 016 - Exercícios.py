#Exercício 1, palíndromo

'''n = int(input("Digite um número maior que 10: "))

aux = n
dig = reverso = 0

while aux != 0:
    dig = aux%10
    reverso = reverso*10 + dig
    aux //= 10
if reverso == n:
    print("%i é palíndromo" % (n))
else:
    print("%i não é palíndromo" % (n))'''

#Exercício 2, sequência
'''n = int(input("Digite o tamanho da sequência: "))
ant = int(input("Digite o número 1: "))
cont = seg = segMAX = 1
while cont < n:
    prox = int(input("Digite o número %i: " % (cont+1)))
    if prox > ant:
        seg += 1
    else:
        if seg > segMAX:
            segMAX = seg
        seg = 1

    cont += 1
    ant = prox

print('O maior segmento crescente da sequência é %i' % (segMAX))'''

#Exercício 3
'''n = 1000
while n < 10000:
    aux = n

    ultimos = aux % 100

    aux //= 100

    primeiros = aux

    if (ultimos + primeiros)**2 == n:
        print(n)

    n += 1'''
#Exercício 4

p = int(input("Digite o valor de p: "))
q = int(input("Digite o valor de q: "))
#Calcula o número de digitos de p
auxp = p
contd = 0
while auxp != 0:
    auxp //= 10
    contd += 1

comparando = True
auxq = q
while comparando:
    subnum = auxq%(10**contd)
    if subnum == p:
        comparando = False

    auxq //= 10
    if auxq == 0:
        comparando = False

if subnum == p:
    print("%i é subnumero de %i" % (p,q))
else:
    print("%i não é subnumero de %i" % (p, q))

