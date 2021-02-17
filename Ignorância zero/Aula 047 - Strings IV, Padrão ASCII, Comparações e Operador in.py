#Exercício 1
'''
def main():
    lista = ['Telefonou para a vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ', 'Devia para a vítima? ','Já trabalhou com a vítima? ']
    classificação = ["Inocente", "Inocente", "Suspeita", "Cúmplice",
                     "Cúmplice", "Assassina"]
    resposta = []
    print("Responda as seguintes perguntas: ")
    for i in lista:
        respostas = str(input(i)).upper()
        resposta.append(respostas)
    contasim = 0
    for k in resposta:
        if k == 'SIM':
            contasim += 1

    if contasim == 2:           #Meu jeito
        print("suspeita")
    elif contasim == 3 or contasim == 4:
        print('Cumplice')
    elif contasim >= 5:
        print('Assassino')
    else:
        print('Inocente')       #


    print(classificação[contasim])
main()
'''

#Exercício 2
'''
def main():
    turno = str(input("Digite o turno em que você estuda: ")).upper()
    while turno != 'V' and turno != 'N' and turno != 'M':
        turno = str(input("Digite o turno correto: ")).upper()
    if turno == 'M':
        print('Bom dia!')
    elif turno == 'V':
        print('Boa tarde!')
    else:
        print('Boa noite!')

main()
'''
'''
for i in range(256):
    print(f'{i:3} - {chr(i)}')
'''
'''
função ord() , que recebe uma letra como parâmetro e retorna o código ASCII da mesma
função chr() , onde passamos o código ASCII e nos é retornado a respectiva letra.
'''
def main():
    string = 'CHiCleTe'

    print(tudoMinusculo(string))
    print(tudoMaiusculo(string))

def tudoMinusculo(string):
    minusculo = ''

    for char in string:
        if 'A' <= char <='Z':
            char = chr(ord(char) + (ord('a') - ord('A')))
        minusculo += char

    return minusculo

def tudoMaiusculo(string):
    maiusculo = ''

    for char in string:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - (ord('a') - ord('A')))
        maiusculo += char

    return maiusculo

main()