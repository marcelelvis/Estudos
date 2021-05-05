#Primeiro exemplo usando booleana
'''dia = int(input("Digite um número para o dia da semana: "))

verifica = False
if dia == 1:
    print("Domingo")
    verifica = True
if dia == 2 :
    print("Segunda")
    verifica = True
if dia == 3:
    print("Terça")
    verifica = True
if dia == 4:
    print("Quarta")
    verifica = True
if dia == 5:
    print("Quinta")
    verifica = True
if dia == 6:
    print("Sexta")
    verifica = True
if dia == 7:
    print("Sábado")
    verifica = True
if verifica != True:
    print("Valor errado")'''

#Exemplo dois usando elif

'''dia = int(input("Digite um dia da semana: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado")
else:
    print("Entrada invalida")'''


#Usando elif e if
#Sem elif

'''num = int(input("Digite um número: "))
if num < 15:
    print("Menor que 15")  #ele irá ver as duas condições
if num < 20: 
    print("Menor que 20")'''
#Com elif
'''num = int(input("Digite um número: "))
if num < 15:
    print("Menor que 15")
elif num < 20:
    print("Menor que 20")    #Com elif, se a primeira condição é atendida ele não vai para a próxima'''


#Escrever os números em forma descrecente
'''a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >= b >= c:
    print(a,b,c)
elif a >= c >= b:
    print(a,c,b)
elif b >= a >= c:
    print(b,a,c)
elif b >= c >= a:
    print(b,c,a)
elif c >= a >= b:
    print(c,a,b)
else:
    print(c,b,a)'''

#Exercício casa 1


#Exercicio dois, programa que leia 3 numeros e diga o maior e menor deles

'''a = int(input("Primeiro numero: "))
b = int(input("Segundo numero: "))
c = int(input("Terceiro numero: "))

if a > b > c:
    print(f'Maior {a} e menor {c}')
elif a > c > b:
    print(f'Maior {a} e menor {b}')
elif b > a > c:
    print(f'Maior {b} e menor {c}')
elif b > c > a:
    print(f'Maior {b} e menor {a}')
elif c > a > b:
    print(f'Maior {c} e menor {b}')
else:
    print(f'Maior {c} e menor {a}')'''

num = int(input("Digite o numero: "))
aux = num
if num < 1000:
    centenas = aux // 100
    aux = aux % 100

    dezenas = aux // 10
    aux = aux % 10

    unidades = aux // 1

    if num >= 100:
        if centenas > 1:
            if dezenas > 1:
                if unidades > 1:
                    print(num, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidades")
                else:
                    print(num, "=", centenas, "centenas,", dezenas, "dezenas e", unidades, "unidade")
            else:
                if unidades > 1:
                    print(num, "=", centenas, "centenas,", dezenas, "dezena e", unidades, "unidades")
                else:
                    print(num, "=", centenas, "centenas,", dezenas, "dezena e", unidades, "unidade")
        else:
            if dezenas > 1:
                if unidades > 1:
                    print(num, "=", centenas, "centena,", dezenas, "dezenas e", unidades, "unidades")
                else:
                    print(num, "=", centenas, "centena,", dezenas, "dezenas e", unidades, "unidade")
            else:
                if unidades > 1:
                    print(num, "=", centenas, "centena,", dezenas, "dezena e", unidades, "unidades")
                else:
                    print(num, "=", centenas, "centena,", dezenas, "dezena e", unidades, "unidade")

    elif 10 <= num < 100:
        if dezenas > 1:
            if unidades > 1:
                print(num, "=", dezenas, "dezenas e", unidades, "unidades")
            else:
                print(num, "=", dezenas, "dezenas e", unidades, "unidade")
        else:
            if unidades > 1:
                print(num, "=", dezenas, "dezena e", unidades, "unidades")
            else:
                print(num, "=", dezenas, "dezena e", unidades, "unidade")
    else:
        if unidades > 1:
            print(num, "=", unidades, "unidades")
        else:
            print(num, "=", unidades, "unidade")
else:
    print("O numero é maior ou igual a mil, o programa nao pode ser executado")

#Elifs tem ligações um com o outro
#if não tem ligações, ou seja, uma condição ser verdadeira não faz o programa parar