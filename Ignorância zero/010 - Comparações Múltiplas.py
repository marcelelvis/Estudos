#Primeiro exemplo
'''idade = int(input("Digite sua idade: "))

if idade >= 18:
    if idade < 70:
        print("Você pode receber o benefício")
    else:
        print("Você não pode receber o benefício")
else:
    print("Você não pode receber o benefício")'''

#Segundo exemplo
'''idade = int(input("Digite sua idade: "))

if 18 <= idade < 70:
    print("Você pode receber o benefício")
else:
    print("Você não pode receber o benefício")'''

#Exercício aula

saque = int(input("Qual valor do saque? "))
print("Serão fornecidas notas de 1, 5, 10, 50 e 100 reais.")
duzentos = saque//200
cem = saque%200//100
cinquenta = saque%100//50
dez = saque%50//10
cinco = saque%10//5
um = saque%5//1

if 9 < saque < 601:
    print(f"Você recebeu {duzentos} nota(s) de 200R$")
    if saque % 200 > 0:
        print(f"Você recebeu {cem} nota(s) de 100R$")
        if saque % 100 > 0:
            print(f"Você recebeu {cinquenta} nota(s) de 50R$")
            if saque % 50 > 0:
                print(f"Você recebeu {dez} nota(s) de 10R$")
                if saque % 10 > 0:
                    print(f"Você recebeu {cinco} nota(s) de 5R$")
                    if saque % 5 > 0:
                        print(f"Você recebeu {um} nota(s) de 1R$")
    print(f"Você sacou {saque}")
else:
    print("O saque deve conter o valor entre 10R$ e 600R$")
