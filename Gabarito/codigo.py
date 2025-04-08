import pyautogui 
pyautogui.PAUSE = 0.4 #Definindo o tempo de espera entre as acções
import time # controle de tempo

# pyautogui. click -> clicar em algum lugar
# pyautogui.write -> escrever algo
# pyautogui.press -> apertar uma tecla
# pyoutogui.hotkey -> apertar teclas juntas

# Passo 1: Enttrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#digitar o sitepythonimpresssionador@gmail.com 
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" 
pyautogui.write(site)
pyautogui.press("enter")

#esperar o site por 3 segundospythonimpresssionador@gmail.com   
time.sleep(3)


#========================================================================='
# Passo 2:fazer login
pyautogui.press("tab")
pyautogui.click(x=763, y=396)
time.sleep(3)
#pyautogui.click(x=766, y=385)
pyautogui.write("testenaldex@gmail.com")
pyautogui.press("tab")
time.sleep(3)
pyautogui.write("Teste123#")
pyautogui.press("enter")
time.sleep(3)


# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv") # ler a base de dados

print(tabela)

# PAsso 4: Cadastrar 1 produto
#time.sleep(3)
pyautogui.click(x=684, y=280)

codigo = "MOLO000251"
pyautogui.write(codigo)

pyautogui.press("tab")
marca = "Logitech"
pyautogui.write(marca)
pyautogui.press("tab")
tipo = "Mouse"
pyautogui.write(tipo)
pyautogui.press("tab")
categoria = "1"
pyautogui.write(categoria)
pyautogui.press("tab")
preco_unitario = "25.95"
pyautogui.write(preco_unitario)
pyautogui.press("tab")
custo = "6.50"
pyautogui.write(custo)
pyautogui.press("tab")
obs = ""
pyautogui.write(obs)
pyautogui.press("tab")
pyautogui.press("enter")




pyautogui.scroll(100000)
# Passo 5: Repetir para todos os produtos

# pyautogui -> automatizações em python 