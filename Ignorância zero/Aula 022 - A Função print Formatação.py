#Exemplo 1
'''
num = int(input("Digite o número de temperaturas registradas: "))

soma = maior = menor = float(input("Digite a temperatura 1: "))


for i in range(2,num+1):
    temp = float(input("Digite a temperatura %d: "%i))

    if temp > maior:
        maior = temp

    if temp < menor:
        menor = temp

    soma += temp

print("A maior temperatura é %6.2f ºC"%maior)
print("A menor temperatura é %6.2f ºC"%menor)
print("A média das temperaturas é %6.2f ºC" %(soma/num))
'''

#Exemplo 2
'''
turma = int(input("Digite o número de turmas: "))
soma = 0

for i in range(1,turma+1):
    alunos = int(input("Digite o número de alunos da turma %d: " % i))
    while alunos <= 0 or alunos > 40:
        print("Número invalido")
        alunos = int(input("Digite o número de alunos da turma %d: "%i))
    soma += alunos
    media = soma/turma
print("A média de alunos por tuma é %.3g"%media)
'''

#Exercício 1
'''
salario = float(input("Digite o salário do funcionário: "))

if salario <= 280:
    aum1 = salario * .20
    print("Salário antes do reajuste era %g" % salario)
    print("Percentual do aumento aplicado foi 20%")
    print("Valor do aumento foi %.2f" % aum1)
    print("O novo salário é %.2f" % (aum1 + salario))
elif salario > 280 and salario < 700:
    aum2 = salario * .15
    print("Salário antes do reajuste era %g" % salario)
    print("Percentual do aumento aplicado foi 15%")
    print("Valor do aumento foi %.2f" % aum2)
    print("O novo salário é %.2f" % (aum2 + salario))
elif salario > 700 and salario < 1500:
    aum3 = salario * .10
    print("Salário antes do reajuste era %g" % salario)
    print("Percentual do aumento aplicado foi 10%")
    print("Valor do aumento foi %.2f" % aum3)
    print("O novo salário é %.2f" % (aum3 + salario))
else:
    aum4 = salario * .05
    print("Salário antes do reajuste era %g" % salario)
    print("Percentual do aumento aplicado foi 5%")
    print("Valor do aumento foi %.2f" % aum4)
    print("O novo salário é %.2f" % (aum4 + salario))
'''

#Exercício 2

maior = 0
menor = 99
for i in range(1,3):
    numalu = float(input("Digite o número do aluno %i: " % i))
    alturaalu = float(input("Digite a altura do aluno %i: " % i))
    if alturaalu > maior:
        maior = alturaalu
        num2 = numalu
    if alturaalu < menor:
        menor = alturaalu
        num3 = numalu
print(f"O número do aluno maior é {num2} e sua altura é {maior:.2f}")
print("O número do aluno menor é %i e sua altura é %.2f"%(num3,menor))
