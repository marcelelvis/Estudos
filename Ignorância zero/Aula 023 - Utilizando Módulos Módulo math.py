'''
import math #Importou toda a bibliotéca

print(math.sin(1))
print(math.cos(2))
print(math.tan(3))
print(math.pow(2,2))
print(math.sqrt(4))
'''

'''
from math import sin #Importei apenas a função Sin do modulo math

print(sin(1))
'''
'''
import math as m #Importei math e dei o nome de m

print(m.sin(1))
print(m.cos(2))
print(m.tan(3))
print(m.pow(2,2))
print(m.sqrt(4))
'''
'''
from math import sin as s #Importei a função sin do modulo math e nomei ela de s

print(s(1))
'''
from math import pi
raio = float(input("Digite o raio do circulo: "))

area = pi*raio*raio

print("A área do circulo de Raio %.10g é %.10g" % (raio, area))