'''class meuobjeto:
    def __init__(self): #criar metódo construtor
        self.nome = 'Marcel' #Criando atributos
        self.idade = 45
        print('Construtor chamado com sucesso')
    def imprime(self):
        print(f'Olá meu nome é {self.nome} e eu tenho {self.idade} anos')

Marcel = meuobjeto()

Marcel.imprime()#Chamando o metodo imprime

class meuobjetob:
    def __init__(self, n, i):
        self.nome = n
        self.idade = i
        print('Construtor chamado com sucesso')
    def imprimi(self, x):#Sempre que quiser uma instancia chame o metodo tem que por 'self'
        print(f'Olá meu nome é {self.nome} e eu tenho {self.idade} anos')
        print(x)

anderson = meuobjetob('Anderson',24)

anderson.imprimi(7)'''
#Exercício 3
'''class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        print('Construtor chamado com sucesso.')
    def envelhecer(self):
        if self.idade < 21:
            while self.idade < 21:
                self.altura += 0.5
                self.idade += 1
        self.idade += 1
    def engordar(self):
        self.peso += 5
    def emagrecer(self):
        self.peso -= 5
    def crescer(self):
        self.altura += .05
    def imprime(self):
        print(f'Meu nome é  {self.nome}, tenho {self.idade} anos, {self.peso}kg e {round(self.altura,2)} de altura')

def main():
    Marcel = Pessoa('Marcel',24, 65, 1.87)
    des = input('Deseja engordar(e), emagrecer(m), crescer(c) ou envelhecer(v) a pessoa? ').upper()
    if des == 'ENGORDAR' or 'E':
        Marcel.engordar()
    elif des == 'EMAGRECER' or 'M':
        Marcel.emagrecer()
    elif des == 'CRESCER' or 'C':
        Marcel.crescer()
    elif des == 'ENVELHECER' or 'V':
        Marcel.envelhecer()

    Marcel.imprime()

main()'''

class quadrado:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def vlado(self):
        return self.lado1, self.lado2

    def mudalado(self):
        self.lado1 += 2
        self.lado2 += 2
        return self.lado1, self.lado2
    def cal(self):
        a = self.lado1
        b = self.lado2
        return a*b

teste = quadrado(3,4)
print(teste.cal())




