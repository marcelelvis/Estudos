contato = {'Nome': 'Marcel', 'Telefone': 123456, 'Endereço': 'Travessa Carlos Sampaio',
           'Email': 'Marcel.elvis11@gmail.com'}
#Metodo get
#recebe um dicionário e uma chave, caso a chave esteja no dicionário ele devolve o valor dela, caso contrário
#devolve um valor defenido

#função criada -->
'''def get(dic, key, value = None):
    if key in dic:
        return dic[key]
    else:
        return value

print(get(contato, 'Nome'))
print(get(contato, 'Celular',88888888))

#Funçao do python
print(contato.get('Email',0))'''

#Imrpime a lista em forma de tupla, função 'items'
#Essa função serve para impressão
#Função com a lógica
'''def items(dic):
    lista = []
    for key in dic:
        lista.append((key, dic[key]))

    print(lista)


print(items(contato))'''
'''#Função do python -->
print(contato.items())

for i in contato.items():#Percorrendo ele no for
    print(i)
for i, j in contato.items():#Percorrer a chave e o valor da chave
 print(i, j)'''
#Função com a lógica
##função key, Cria uma lista com as chaves
'''def keys(dic):
    lista = []
    for key in dic:
        lista.append(key)

    print(lista)

print(keys(contato))'''
#função do python
'''print(contato.keys())
for i in contato.keys():
    print(i)'''
#Função com a lógica
#Cria uma lista com os valores da chave
'''def values(dic):#Vai pegar o valor do dicionário
    lista = []
    for key in dic:
        lista.append(dic[key])

    print(lista)

print(values(contato))'''

#Função do python
'''print(contato.values())
for i in contato.values():
    print(i)'''
#Explicação de cada função -->
'''contato2 = contato.copy()#funçao copy, copia o dicionário

contato2[11] = 11

contato2.pop(11)#função pop, exclui uma chave do dicionário

contato2.popitem()#função popitem: remove o primeiro item do dicionário e retorna ele como tupla, não recebe argumento

contato2.clear()#Função clear: apaga todo o dicionário

contato.setdefault('Nome')#Função setdefault: caso a chave exista, ele retorna o valor dela
contato.setdefault('Lucas', 123)#caso ela não exista, ele cria ela com o valor None'''



