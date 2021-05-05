Pessoa = {'Nome': 'Lucas', 'Empergo': 'Advogado', 'Idade': 20, 'Cor de cabelo': 'Preto'}

class Pessoa:
    pass

Lucas = Pessoa()

Lucas.nome = 'Lucas'
Lucas.emprego = 'Advogado'
Lucas.CordeCabelo = 'Preto'
a = Lucas.__dict__ #Transforma em dicionário

print(a)
a = input("Digite")