contato = {'Nome': 'Marcel', 'Telefone': 27639034, 'Celular': 968702266, 'Email': 'Marcel.elvis11@gmail.com'}

print(contato['Nome'])

dic = {4.7783: 'O que é isso?!'}

print(dic[4.7783])

dicionariodecontatos = {'contato1': contato}

print(dicionariodecontatos['contato1'])

contato['Endereço'] = 'Travessa Carlos Sampaio'

print(contato)

#Imprime os valores do dicionário
for i in contato:
    print(contato[i]) #print(contato)'Imprime as chaves'