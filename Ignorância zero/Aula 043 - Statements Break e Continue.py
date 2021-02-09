#Exemplo 1
'''
def criaLista():
    lista = []

    m = int(input("Digite o tamanho da lista: "))

    for i in range(m):
        ele = float(input(f"Digite o elemento {i+1} de {m}: "))
        lista.append(ele)

    return lista

def main():
    l1 = criaLista()

    n = int(input("Digite o número de elementos que se deseja somar: "))

    soma = 0
    for i in range(len(l1)):
        if i == n:
            break
        soma += l1[i]
    print(f"A soma é {soma}")

main()
'''

#Exemplo 2
