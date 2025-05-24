'''Um programa que leia um número de no máximo 4 digitos  e mostre na tela um dos dígitos separados.
Ex:
Digite um número: 1234
unidade: 4
dezena: 3
centena: 2
milhar: 1
'''
#tentando por string
numero = str(input('Digite um número de 4 dígitos: \n'))
if len(numero) > 4:
    print ('Número inválido!')
else:
    print(f'Unidade: {numero[3]}')
    print(f'Dezena: {numero[2]}')
    print(f'Centena: {numero[1]}')
    print(f'Milhar: {numero[0]}')

#Tentando por inteiro
num = int(input('Digite um valor de no méximo 4 dígitos: \n'))
print(f'Unidade: {num // 1 % 10}')  #Resto da divisão por 1, depois o resto da divisão por 10
print(f'Dezena: {num // 10 %10}')   #Resto da divisão por 10, depois o resto da divisão por 10
print(f'Centana: {num //100 % 10}') #Resto da divisão por 100, depois o resto da divisão por 10
print(f'Milhar: {num //1000 % 10}') #Resto da divisão por 1000, depois o resto da divisão por 10