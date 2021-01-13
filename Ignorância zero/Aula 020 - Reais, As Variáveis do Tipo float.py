#Exemplo 1
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = ((nota1+nota2+nota3)/3)

if media == 10:
    print("Aprovado  com distinção")
elif media < 7:
    print("Reprovado")
elif media >= 7:
    print("Aprovado")
'''

#Exercício 2

a = float(input("Digite o valor de a: "))
if a > 0:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c
    raizp = (-b + (delta**(1/2)))/(2*a)
    raizn = (-b - (delta**(1/2)))/(2*a)

    if delta < 0:
        print("Equação não possui raízes")
        quit()
    elif delta == 0:
        print("Só possui uma raiz", raizp)
    else:
        print("Possui duas raízes e elas são: %d e %d" % (raizp, raizn))
else:
    print("Não é equação do segundo grau")
