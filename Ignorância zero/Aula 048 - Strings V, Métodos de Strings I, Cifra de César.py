'''
Isalpha() = Verefica se todos os caracteres dentro de uma string são letras ou não
islower() = Verefica se todos os caracteres dentro de uma string são minusculos
isupper() = Verefica se todos os caracteres dentro de uma string são maiusculos

'''


TAM_MAX_CH = 26
def recebeModo():
    while True:
        modo = input("Você deseja criptografar ou decriptografar?\n").lower()
        if modo in "Entra 'criptografar' ou 'c' ou 'decriptografar' ou 'd'".split(' ou '):
            return modo
        else:
            print("Entra 'criptografar' ou 'c' ou 'decriptografar' ou 'd'")

def recebeChave():
    global TAM_MAX_CH

    while True:
        chave = int(input(f"Entre com o número da chave (1-{TAM_MAX_CH})\n"))

        if 1 <= chave <= TAM_MAX_CH:
            return chave

def geraMsgTraduzida(modo, mensagem, chave):
    global TAM_MAX_CH
    if modo[0] == 'd':
        chave *= -1
    traduzido = ''
    for simbolo in mensagem:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= TAM_MAX_CH
                elif num < ord('A'):
                    num += TAM_MAX_CH
            elif simbolo.islower():
                if num > ord('Z'):
                    num -= TAM_MAX_CH
                elif num < ord('A'):
                    num += TAM_MAX_CH
            traduzido += chr(num)
        else:
            traduzido += simbolo
    return traduzido


def main():

    modo = recebeModo()
    mensagem = input("Entre sua mensagem\n")
    chave = recebeChave()

    print(f'Seu texto traduzido é: ')
    print(geraMsgTraduzida(modo, menasgem, chave))

main()