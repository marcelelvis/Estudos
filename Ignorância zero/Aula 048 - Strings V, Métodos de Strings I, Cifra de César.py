TAM_MAX_CH = 26
def recebeModo():
    while True:
        modo = input("Você deseja criptografar ou decriptografar?\n").lower()
        if modo in "Entra 'criptografar' ou 'c' ou 'decriptografar' ou 'd'".split(' ou '):
            return modo
        else:
            print("Entra 'criptografar' ou 'c' ou 'decriptografar' ou 'd'")

def recebeChave():