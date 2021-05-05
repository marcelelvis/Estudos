'''class Mamifero:
    def __init__(self, cordepelo, genero, andar):
        self.cordepelo = cordepelo
        self.genero = genero
        self.numdepatas = andar
    def falar(self):
        print("Olá sou um mamifero e eu sei falar")
    def andar(self):
        print(f"Estou andando sobre {self.numdepatas}")
    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print("Machos não amamentam")
            return
        print("Amamentando meu filhote")

class Pessoa(Mamifero):
    def __init__(self,cordepelo, genero, andar, cabelo):
        # Herança peguei isso tudo aqui, dessa forma, n precisar redefinir esses atributos ->
        Mamifero.__init__(self,cordepelo, genero, andar)
        self.cabelo = cabelo
    def falar(self):
        print('Eu sei falar')
julia = Mamifero('preto', 'feminino', 4)

print(julia.falar())'''

class objetografico(object):
    def __init__(self, cordepreenximento, preenxida, cordecontorno):
        self.cordepreenximento = cordepreenximento
        self.preenxida = preenxida
        self.cordecontorno = cordecontorno
class retangulo(objetografico):
    def __init__(self, cordepreenximento, preenxida, cordecontorno, base, altura):
        objetografico.__init__(self, cordepreenximento, preenxida, cordecontorno)
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return self.base + self.altura
from math import pi
class circulo(objetografico):
    def __init__(self, cordepreenximento, preenxida, cordecontorno,raio):
        objetografico.__init__(self, cordepreenximento, preenxida, cordecontorno)
        self.raio = raio
    def area(self):
        return self.raio**2 * pi
    def perimetro(self):
        return self.raio * 2 * pi
class triangulo(objetografico):
    def __init__(self, cordepreenximento, preenxida, cordecontorno, base, altura):
        objetografico.__init__(cordepreenximento, preenxida, cordecontorno)
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return self.base + self.altura