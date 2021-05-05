'''
def main():
    print("Comparativo de Consumo de Combustível\n")

    lista = []

    for i in range(2):
        print("Veículo %i"%(i+1))
        nome = input("Nome: ")
        km = float(input("Km por Litro: "))
        lista.append([nome, km])

    print("\nRelatório Final")

    saidas = []

    for i in range(2):
        saidas.append(' %i - '%(i+1))

        #Nomes
        x = lista[i][0]
        Formata1(i, x, 16, saidas)

        saidas[i] +=' - '

        #Km por litro
        x = "%.1f"%lista[i][1]
        Formata2(i, x, 6, saidas)

        saidas[i] +=' - '

        #Litros a cada mil km
        x = "%.1f"%(1000/lista[i][1])
        Formata2(i, x, 6, saidas)

        saidas[i] += " litros - R$ "

        #R$ a cada mil km
        x = "%.2f"%(2250/lista[i][1])
        Formata2(i, x, 6, saidas)

        #Imprimindo Tudo
        print(saidas[i])


def Formata1(i, palavra, lmt, saida):
    if len(palavra) <= lmt:
        saida[i] += palavra + (lmt - len(palavra))*" "


def Formata2(i, palavra, lmt, saida):
    if len(palavra) <= lmt:
        saida[i] += (lmt - len(palavra))*" " + palavra

main()
'''

def main():
    tudo = []

    for i in range(2):
        print(f"Veículo {i+1}")
        carro = str(input("Nome: "))
        km = float(input("Km por litro: "))
        tudo.append([carro, km])
    print("Relatório Final")
    for k in range(2):
        print(f"{k+1} - {tudo[k][0]:10} - {tudo[k][1]:6} - {1000/tudo[k][1]:7.1f} litros - R${2250/tudo[k][1]:7.2f}")

main()