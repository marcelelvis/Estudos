#exercicio 1, potencia

'''base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

cont = 0
produto = 1
while cont < expoente:
    produto = produto*base
    cont = cont + 1
print(f'{base} elevado a {expoente} = {produto}')'''

#Exercicio 2, fatorial

'''fat = int(input("Digite um valor: "))
aux = fat
cont = fat-1
while cont > 1:
    aux = aux * cont
    cont = cont - 1
print(aux)'''

#EXercicio 3, potencia
'''
a = int(input("Digite um valor"))
while a != 0:
    print(f'{a} ao quadrado = {a*a}')
    a = int(input("Digite o próximo número: "))'''

while True:
    a = int(input("Digite um número: "))
    cont = 0
    aux = -1
    if a == 0:
        print("Você parou o programa")
        break
    if a > 0:
        while cont < a:
            if aux % 2 != 0:
                aux += 2
            cont += 1
            print(aux)
    else:
        print("Digite um valor válido")


