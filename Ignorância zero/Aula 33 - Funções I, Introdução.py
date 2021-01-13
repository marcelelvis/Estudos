#Exemplos funções
'''
def potencia(base, exp):
    pot = base**exp
    return pot

print(potencia(2,3))

def soma (s1, s2, s3):
   return s1+s2+s3

print(soma(2,4,6))
'''
'''
def somaimposto(taxa, custo):
    t = taxa*custo/100
    return cst+t

cst = int(input("Digite o custo do produto: "))
tx = int(input("Digite a taxa do imposto: "))
print(f"O valor do produto é {somaimposto(tx, cst):.0f}")
'''

def conver(hora, minuto):
    if hora <= 12:
        trocado = hora + 12
        print(f"São {trocado}:{minuto}AM")
    else:
        trocado2 = hora - 12
        print(f"São {trocado2}:{minuto}PM")
rodando = True
while rodando:
    horas = int(input("Que horas são: "))
    minutos = int(input("Quantos minutos são: "))
    conver(horas, minutos)
    rodando = bool(int(input("Quer continuar? Sim[1]/Não[0] ")))
    print()


