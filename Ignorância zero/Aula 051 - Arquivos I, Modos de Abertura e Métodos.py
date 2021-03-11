'''arquivo = open('OlaArquivo.txt', 'w') #Abrir o arquivo e escrever nele

#Modos de abertura
# w --> write --> Escrever #Escreve dentro do arquivo
# r --> read --> ler #Abre o arquivo no python
# a --> append --> extender

arquivo.write('Chiclete com Banana')
arquivo.write('\n')
arquivo.write('Manga com Leite')

#arquivo.writelines(['Olá', 'arquivo', 'essa', 'é', 'nossa', 'primeira', 'aula']) #Recebe uma lista

#Sempre fechar o arquivo no final

arquivo.close()'''

'''arquivo = open('OlaArquivo.txt', 'r') # 'r' Não é necessário pois é um padrão do metodo open

print(arquivo.read())


x = arquivo.readline() #Ler linha por linha 'readline'
x = arquivo.readlines() #Ler todas a linhas e cria uma lista separando elas 'readlineS'

arquivo.close()

arquivo = open('OlaArquivo.txt', 'a') #Modo append
'''
a = [['teste', 'mostrando', 'vereficar']]

for i in 'Pedro':
    print(i)