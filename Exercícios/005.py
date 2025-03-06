'''
Este projeto é uma calculadora de imc mais precisa
Ela calcula o imc também de acordo com o gênero do usuário
'''

genero = input('Qual o seu gênero?\nDigite [H]omem ou [M]ulher:\n').strip().lower()

if not genero:
    print('Você não preencheu o campo gênero')
    exit()
elif genero not in['h','m']:
    print('Gênero inválido')
    exit()


nome = input('Qual o seu nome?\n').strip()
peso = input('Qual o seu peso em Kg?\n').strip()
altura = input('Digite sua altura em m.\n').strip()


try:
    float_peso = float(peso)
    float_altura = float(altura)
    imc = float_peso / (float_altura ** 2)
    
    print(f'{nome}, o seu imc é:{imc:.2f}')
    

    if genero == 'h': 
        if imc < 20:
            print(f'{nome}, você está abaixo do peso normal')
        elif imc >=20 and imc < 24.9:
            print(f'{nome}, você está no peso ideal.')
        elif imc >=24.9 and imc < 29.9:
            print(f'{nome}, você está com obesidae leve.')
        elif imc >= 29.9 and imc <39.9:
            print(f'{nome}, você está com obesidade moderada')
        else:
            print(f'{nome} você está com obesidade mórbida.')
    
    elif genero == 'm':
    
        if imc < 19:
            print(f'{nome}, você está abaixo do peso normal')
        elif imc >=19 and imc <23.9:
            print(f'{nome}, você está no peso ideal.')
        elif imc >= 23.9 and imc <28.9:
            print(f'{nome}, você está com obesidade leve.')
        elif imc >= 28.9 and imc <38.9:
            print(f'{nome}, você está com obesidade moderada')
        else: 
            print(f'{nome} você está com obesidade mórbida.')

except ValueError:
    print('Erro: Insira valores válidos para peso e altura')
    