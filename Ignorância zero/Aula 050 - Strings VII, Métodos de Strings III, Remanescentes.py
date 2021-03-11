#funções find e index
#Ambas dizem se uma string é substring de outra

'''def find(frase, sub):
    for i in range(len(frase) + 1 - len(sub)):
        if frase[i:i+len(sub)] == sub:
            return i

    return None

#funçao do python
'Mississipi'.find('a')

def index(frase, sub):
    for i in range(len(frase) + 1 - len(sub)):
        if frase[i:i+len(sub)] == sub:
            return i

    return 'Erro'

#funçao do python
'Mississipi'.index('a')
'''

#Count conta o número de ocorrências de uma substring em uma string

'''def find(frase, sub):
    for i in range(len(frase) + 1 - len(sub)):
        cont = 0
        if frase[i:i+len(sub)] == sub:
            cont += 1
    return cont

#funçao do python
'Mississipi'.count('ss')'''

#Replace recebe uma substring velha e uma substring nova, toda vez que encontrar uma substring velha
#ele substitui pela nova

#funçao do python
'''rio = 'mississipi'
rio.replace('ss','zz')

def replace(frase, velha, nova):
    palavra = ''
    i = 0
    while i < len(frase) + 1 - len(velha):
        if frase[i:i+len(velha)] != velha:
            palavra += frase[i]
        else:
            i += len(velha)
            palavra += nova
            continue
        
        i+= 1
    palavra += frase[i:]
    return palavra'''

