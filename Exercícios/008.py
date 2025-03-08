'''
Faça um programa que peça ao usuário para digitar um número inteiro,
Informe se este númeri é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro
'''

try:
    entrada = (input('Digite um número inteiro.\n'))
    if not entrada:
        print('Você não inseriu um número')
    else:
        numero = int(entrada) #Tenta converter a entrada para um intero
        resto = numero % 2
        if resto == 0:
            print(f'O resto da divisão por dois é: {resto}, então {numero} é par')
        else:
            print(f'O resto da divisão por dois é: {resto}, então {numero} é ímpar') 
except:
    print(f'{numero} não é um número inteiro')
    exit()