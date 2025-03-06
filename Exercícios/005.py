'''
Este projerto é uma calculadora de imc mais precisa
Ela calcula o imc também de acordo com o gênero do usuário
'''
genero = input('Qual o seu gênero?\n'
               'Digite [H]omem ou [M]ulher:\n').strip().lower()
nome = input('Qual o seu nome?\n').strip()
peso = input('Qual o seu peso?\n').strip()
altura = input('Digite sua altura\n').strip()

#converti os valores do peso e da altura, que estavam como str para float
float_peso = float(peso)
float_altura = float(altura)
imc = float_peso / float_altura ** 2

if not genero:
    print('Você ')

if  not genero.strip():
    print('Você não preencheu o campo gênero.')
elif genero == 'H' or genero=='h':
    print(f'{nome}, O seu imc é:{imc:.2f}')
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
            
elif genero =='M' or genero == 'm':
    print(f'{nome}, O seu imc é:{imc:.2f}')
    if imc < 19:
        print(f'{nome}, você está abaixo do peso normal')
    elif imc >=19 and imc <23.9:
        print(f'{nome}, você está no peso ideal.')
    elif imc >= 23.9 and imc <28.9:
        print(f'{nome}, você está com obesidae leve.')
    elif imc >= 28.9 and imc <38.9:
        print(f'{nome}, você está com obesidade moderada')
    else: 
        print(f'{nome} você está com obesidade mórbida.')
else:
    print('Gênero invalido')