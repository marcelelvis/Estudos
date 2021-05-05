class Conta():
    __total = 10000 #Privando atributo com o __
    reserva = .1
    def __init__(self, ID, saldo):
        self.__ID = ID #Privando atributo __
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
        Conta.__total += valor #Privando atributo __
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            Conta.__total -= valor
#Também podemos privar métodos por exemplo o saque, seria def __saque(self, valor):
itau = Conta(12345, 1000)
itau.deposito(500)
Conta.deposito(itau,500)

print(itau.saldo)


'''#Abstração
class obstrair():
    def __init__(self, retangulo):
        self.retangulo = retangulo
    def abstracao(self): #Isso é abstrair
        pass'''

#Exercício

'''class Banco(object):
    __total = 10000
    TaxaReserva = 0.1
    reservaExigida = __total*TaxaReserva

    def podeFazerEmprestimo(valor):
        Banco.__total -= valor
        if Banco.__total >= Banco.reservaExigida:
            pode = True
        else:
            pode = False

        Banco.__total += valor

        return pode

    def MudaTotal(valor):
        Banco.__total += valor

class Conta
    def __init__(self, saldo, ID, senha):
        self.__saldo = saldo
        self.__ID = ID
        self.__senha = senha

    def deposito(self, senha, valor):
        if senha == self.__senha:
            self.__saldo += valor
            Banco.mudaTotal(valor)

    def saque(self, senha, valor):
        if senha == self.__senha:
            self.__saldo -= valor
            Banco.mudaTotal(-valor)

    def podeReceberEmprestimo(self, valor):
        return Banco.podeFazerEmprestimo(valor)

    def saldo(self):
        print(self.__saldo)'''
