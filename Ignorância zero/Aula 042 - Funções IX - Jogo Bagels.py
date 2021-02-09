from tkinter import *
from funçoes import *
class Bagels:
    import random

    ult_dig = (lambda x: x % 10)

    def VerificaEntrada(num):
        if 1000 <= num < 10000:
            return True
        else:
            return False

    def GeraSecretNum():

        numeros = list(range(10))
        secretNum = 0
        while numeros[0] == 0:
            random.shuffle(numeros)  # Função para embaralhar os números

        for i in range(4):
            dig = numeros[i]
            secretNum = dig * (10 ** (3 - i))

        return secretNum, numeros[:4]

    def GeraDicas(num, secretNum, secretNumList):
        global ult_dig
        if secretNum == num:
            return []
        dica = []

        for i in range(4):
            if ult_dig(num) == ult_dig(secretNum):
                dica.append(2)
            elif ult_dig(num) in secretNumList:
                dica.append(1)

        num //= 10
        secretNumList //= 10

        if len(dica) == 0:
            dica.append(0)
        dica.sort()
        return dica