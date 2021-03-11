import random

FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

palavras = 'formiga babuino encefalo elefante girafa hamurger chocolate giroscópio'.split()

def main():
    global FORCAIMG
    print('F O R C A')
    letrasErradas = ''
    letrasAcertadas = ''
    palavraSecreta = geraPalavraAleatória().upper()
    jogando = True

    while jogando:
        imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)

        palpite = recebePalpite(letrasErradas + letrasAcertadas)

        if palpite in palavraSecreta:
            letrasAcertadas += palpite

            if VereficaSeGanhou(palavraSecreta, letrasAcertadas):
                print(f"Exato! A palavra secreta é {palavraSecreta}! Você ganhou!!")
                jogando = False
        else:
            letrasErradas += palpite

            if len(letrasErradas) == len(FORCAIMG) - 1:
                imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta)

                print(f'Você excedeu o seu limite de palpites!')
                print(f'Depois de {str(len(letrasErradas))} letras erradas e {str(len(letrasAcertadas))}', end=' ')
                print(f"Palpites corretos, a palavra era {palavraSecreta}.")

                jogando = False

        if not jogando:
            if JogarNovamente():
                letrasErradas = ''
                letrasAcertadas = ''
                jogando = True
                palavraSecreta = geraPalavraAleatória()

def geraPalavraAleatória():
    global palavras
    return random.choice(palavras)

def imprimeComEspaços(palavra):
    for letra in palavra:
        print(letra, end = ' ')
    print()

def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    global FORCAIMG
    print(FORCAIMG[len(letrasErradas)]+'\n')

    print("Letras Erradas:", end = ' ')
    imprimeComEspaços(letrasErradas)

    vazio = '_'*len(palavraSecreta)

    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]

    imprimeComEspaços(vazio)



def recebePalpite(palpitesFeitos):
    while True:
        palpite = input("Adivinhe uma letra.\n").upper()

        if len(palpite) != 1:
            print("Coloque uma única letra.")
        elif palpite in palpitesFeitos:
            print("Você já chutou essa letra. Escolha novamente.")
        elif not 'A' <= palpite <= 'Z':
            print('Por favor escolha apenas letras.')
        else:
            return palpite

def JogarNovamente():
    return input("Você quer jogar novamente? (sim ou não)\n").upper().startswith('S')

def VereficaSeGanhou(palavraSecreta, letrasAcertadas):

    ganhou = True

    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break

    return ganhou

main()



