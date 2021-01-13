#Exercício 1

n = int(input("Digite o numero de empresas: "))
m = int(input("Digite o numero de meses: "))

empresa = 1
print('')
while empresa <= n:
    mes = 1
    balança = 0
    print(f"Empresa {empresa} :")
    while mes <= m:
        print(f'Mês {mes} :')
        ganho = int(input("Digite o ganho da empresa: "))
        gasto = int(input("Digite o gasto da empresa: "))
        balança = balança + (ganho - gasto)
        print('')
        mes = mes + 1
    if balança == 0:
        print(f'A empresa {empresa} ficou indiferente')
    elif balança > 0:
        print(f'A empresa {empresa} fechou com lucro')
    else:
        print(f'A empresa {empresa} fechou em défice')
    empresa = empresa + 1
    print('')