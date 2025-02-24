# Introdução a f-string
#Calculadore de imc
nome = 'Arnaldo Leão'
altura = 1.81
peso = 63
imc =  64/ 1.81**2 

linha_1 = f'{nome} tem {altura:.2f} de altura' #Caso eu queira fazer formatação como de moedas eu posso fazer ':,.2f
linha_2 = f'pesa{peso}kg e seu imc é:'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)