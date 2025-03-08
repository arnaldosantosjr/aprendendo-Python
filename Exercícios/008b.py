'''
Faça um programa que pergunte a hora ao usuário e , baseando-se no horário descrito, exiba a saudação apropriada. Exe.:
Bom dia 0 - 11, boa tarde 12 - 17 e boa noite 18 - 23.
Os valores dem ser interios 
'''

try:
    entrada = input('Que horas são?\n')
    if not entrada:
        print('Você não inseriu as horas')
        exit()
    else:
        hora = int(entrada)
        if 0 <= hora<= 23:
            print(f'São {hora} horas.')
            if 0 <= hora <= 11:
                print('Bom dia!')
            elif 12 <= hora <= 17:
                print('Boa tarde!')
            else:
                print('Boa noite!')
        else:
            print('Insira um valor entre 0 e 23')
            exit()
except ValueError:
    print('Valor inserido não é válido')