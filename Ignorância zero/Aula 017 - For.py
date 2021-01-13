#Fatorial for
'''
a = int(input())
fat = 1
for i in range(a,1,-1):
    fat *= i
    print(i)
print(fat)
'''
'''
a = int(input())
fat = 1

for i in range(2,a+1):
    fat *= i
print(fat)
'''

#Com while
'''
a = int(input("Digite: "))
cont = 0
fat = 1
while cont < a:
    cont += 1
    fat *= cont
    print(cont)
print(fat)
'''
#Exemplo 2, triangular

'''for i in range(5,51,5): #Calcular o triangular
    triangular = i *(i+1)//2
    print(triangular)'''

eleitores = int(input("Digite o número de eleitores: "))

cand1 = 0
cand2 = 0
cand3 = 0

for ne in range(1,eleitores+1):
    voto = int(input("Eleitor %i: " % (ne)))
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    else:
        while voto != 1 and 2 and 3:
            print("Digite um voto válido: ")
            voto = int(input("Eleitor %i: " % (ne)))
            if voto == 1:
                cand1 += 1
            elif voto == 2:
                cand2 += 1
            elif voto == 3:
                cand3 += 1
print("Candidato 1 teve %i votos" %(cand1))
print("Candidato 2 teve %i votos" %(cand2))
print("Candidato 3 teve %i votos" %(cand3))
