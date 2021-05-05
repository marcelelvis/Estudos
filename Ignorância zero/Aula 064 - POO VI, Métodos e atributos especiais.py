class conta:
    #Objeto do tipo conta, representa uma conta num banco qualquer
    def __init__(self, ID, saldo):
        '''Construtor da classe conta'''
        self.ID = ID
        self.saldo = saldo
    def __str__(self): #Configura o valor que você quer mostrar quando tirar um print
        return f'ID: {self.ID}\nSaldo: {self.saldo}'
    def __add__(self, outro):#O metodo __add__ redefiniu a função de soma '+'
        self.saldo += outro.saldo
    def __call__(self,x):#callable
        return x
    '''Callable, permite uma instância(bradesco = conta(123,400)) de um objeto ser chamada,
     ser um tipo um objeto e pode ser chamada'''



bradesco = conta(456, 5000)
itau = conta(123,8000)
bradesco('Eu sou uma conta')#Graças a callable dá para fazer isso
print(callable(bradesco)) #Retorna se uma instância pode ser chamada

'''print(bradesco,'\n')

itau + bradesco#O metodo __add__ redefiniu a função de soma '+'

print(itau.saldo)
'''

class pai:
    pass
class filha(pai):
    pass
class neta(filha):
    pass

print(issubclass(filha,pai))
'''Retorna um bool, dizendo se uma classe é subclasse de outra'''