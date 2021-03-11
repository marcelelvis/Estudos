'''class Minha:
    def __init__(self):
        self.x = 0
        self.y = 0
meu = Minha()
print(meu.x)

class PessoaS2animais:
    def __init__(self, nome, peso, cao):
        self.nome = nome
        self.peso = peso
        self.cao = cao
    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()

class Cachorro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def daApatinha(self):
            print(f'{self.nome}extendeu a patinha')
    def latir(self):
        print('AUAUAUAUAUAUAUAUA')

rex = Cachorro('Rex', 'marrom')
Marcel = PessoaS2animais('Marcel', 65, rex)'''

class ponto:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    def imprimivalores(self):
        print(self.x)
        print(self.y)
class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def centroret(self):
        x = self.largura / 2
        y = self.altura / 2
        print(f'Valor de x: {x}')
        print(f'Valor de y: {y}')
    def mudavalor(self):
        des = input("Deseja mudar o valor do retangulo?[s/n] ").upper()
        if des == 'S':
            novovalor = input(f"Digite o valor novo largura: ")
            novovalor2 = input(f"Digite o valor novo altura: ")
            self.largura = novovalor
            self.altura = novovalor2
        print(self.largura)
        print(self.altura)



teste = ponto(2,3)
ret = retangulo(4,5)
ret.mudavalor()
ret.centroret()


