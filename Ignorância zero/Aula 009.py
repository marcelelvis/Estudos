#Programa loja de tinta
'''area = int(input("Digite a área a ser pintada: "))

litros = area//3
if area % 3 > 0:
    litros+= 1
latas = litros//18
if litros % 18 > 0:
    latas+= 1

print("Você precisa de", latas, "latas.")
print("Você vai pagar R$", latas*80)'''

#Faça um programa que peça um valor e mostra se é positivo ou negativo
#Ex 2
''''
valor = int(input("Digite um valor: "))
if valor < 0:
    print("Negativo")
else:
    print("Positivo")'''

area = int(input("Digite a área a ser pintada: "))
area = area*.1

litros = area//6
    if litros % 6 != 0:
        litros += 1
latas = litros//18
    if latas % 18 != 0:
        latas += 1
latas4 = litros//4
    if latas4 % 4 != 0:
        latas4 += 1
print("Latas de 18 litros", latas)