import pyautogui #faz a automação de mouse e teclado
import pyperclip #Permite copiar e colar em python
import time #controla o tempo do programa
pyautogui.alert("O programa vai começar, não use o computador")
pyautogui.PAUSE = 1 #FAZ A AUTOMOÇÃO DAR 1 SEC DE PAUSE
pyautogui.hotkey('ctrl','t') #hotkey aperta sequência de botões
link = 'https://drive.google.com/drive/folders/1wRTFw0sUVBjRr4hW5U9LF7DjLixRyxym'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')#PRESS pressiona apenas uma tecla
time.sleep(5) #coloca o python p esperar p executar a próxima instrução
pyautogui.click(-651,688, clicks=2) #da os cliques no mouse de acordo com a posição

'''
pyautogui.click(80,80)

pyautogui.doubleClick(80,80)

pyautogui.rightClick(80,80)
É possível clicar em uma determinada coordenada na tela por meio do método de clique que 
também fornece doubleClick, métodos RightClick pegando os parâmetros 
coordenada x e coordenada y em todos os casos.'''

#Calcular indicadores
#usando biblioteca panda

import pandas as pd
#as serve para apilidar panda de pd para na hora de usar ela abreviar

tabela = pd.read_excel(r"C:\Users\Marcel\Downloads\Vendas - Dez.xlsx", sheet_name=0)#she serve para dizer qual aba ser lida
display(tabela)#Display organiza tudo da tabela
faturamento = tabela["Valor Final"].sum()
qnt_produto = tabela["Quantidade"].sum()

#abrir o email
pyautogui.hotkey('ctrl','t')
link = 'http://mail.google.com/'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(8)

#Escrever o -email
pyautogui.click(-917, 518)
time.sleep(3)

#Escolher o email
pyautogui.write('marcel.elvis11+diretoria@gmail.com')
pyautogui.press('tab')

#Preencher o assunto
pyautogui.press('tab')
Relatorio = 'Relatório de vendas'

pyperclip.copy(Relatorio)
pyautogui.hotkey('ctrl','v')

#Preecher email
pyautogui.press("tab")
textoemail = f"""
Prezado, bom dia

O faturamento de foi: R${faturamento:,.2f}
A quantidade de produtos foi de: {qnt_produto:,}

abs
Elves"""
pyperclip.copy(textoemail)
pyautogui.hotkey('ctrl','v')