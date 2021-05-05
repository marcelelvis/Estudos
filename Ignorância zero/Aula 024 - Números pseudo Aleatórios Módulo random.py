import random
'''
for i in range(10):
    x = random.randrange(1,7)
    print(x)
'''

testes = int(input("Digite o número de testes: "))

trocar = 0
n_trocar = 0

for i in range(testes):
    porta = random.randrange(1,4) #Sorteia a porta
    premio = random.randint(1,3) #Sorteia a porta que o usuário escolheu
    if porta == premio:
       n_trocar += 1
    else:
       trocar += 1

print(f"É vantajoso trocar em {trocar*100/testes:.0f}% das vezes")
print(f"Não é vantajoso trocarm em {n_trocar*100/testes:.0f}% das vezes")
'''
lista = [1,2,4,5,7]

a = random.choice(lista)

print(a)
'''