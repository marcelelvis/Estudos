#Exemplo 1
contas = []
depositos = []
saldo = 0

def main():
    opção = bool(int(input("Deseja criar conta(1) ou fehcar programa(0): ")))
    while opção:
        criaconta()
        versaldo()
        opção = bool(int(input("Deseja criar conta(1) ou fehcar programa(0): ")))
def criaconta():
    global contas, depositos,saldo
    num_conta = int(input("Digite um número de conta: "))

    while num_conta in contas:
        print("Conta já existente. Digite novamente.")
    contas.append(num_conta)

    deposito = float(input("Digite o valor do seu primeiro depósito: "))
    while deposito <= 0:
        print("Valor de depósito inválido.")
        deposito = float(input("Digite o valor do seu primeiro depósito: "))

    depositos.append(deposito)
    saldo += deposito

def versaldo():
    global saldo
    opção = bool(int(input("Deseja ver o saldo do banco(1 - Sim/ 0 - Não) ")))
    if opção:
        print(f"O saldo do banco é R$ {saldo:.2f}")


main()