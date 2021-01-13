#Exemplo 1
'''
int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro"))
real = float(input("Digite um número real: "))

print((2*int1)*(int2/2))
print(3*int1 + real)
print(real**3)
'''

#Exemplo 2
'''
num = float(input("Digite um número: "))

if num != int(num):
    decimal = num - int(num)
    arredondado = int(num)

    if decimal >= 0.5:
        arredondado += 1

    print(num, "é decimal")
    print("Arredondado: ", arredondado)
else:
    print(int(num),"é inteiro")
'''

#Exercício 1

x = float(input("Digite o valor de x: "))
n = int(input("Digite o valor de n: "))

cos = termo = 1

for k in range(1, n+1):
    termo *= (-(x**2))/((2*k*(2*k-1)))
    cos += termo

print(x,cos)
