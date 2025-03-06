'''
Este projeto é uma calculadora de IMC mais precisa.
Ela calcula o IMC também de acordo com o gênero do usuário.
'''

# Solicita o gênero primeiro
genero = input('Qual o seu gênero?\nDigite [H]omem ou [M]ulher:\n').strip().lower()

# Verifica se o campo gênero foi preenchido corretamente
if not genero:
    print('Você não preencheu o campo gênero.')
    exit()  # Encerra o programa imediatamente
elif genero not in ['h', 'm']:
    print('Gênero inválido.')
    exit()  # Encerra o programa imediatamente

# Solicita os outros dados somente se o gênero for válido
nome = input('Qual o seu nome?\n').strip()
peso = input('Qual o seu peso (kg)?\n').strip()
altura = input('Digite sua altura (m)\n').strip()

# Converte peso e altura para float
try:
    float_peso = float(peso)
    float_altura = float(altura)
    imc = float_peso / (float_altura ** 2)

    print(f'{nome}, o seu IMC é: {imc:.2f}')

    # Definição das faixas de IMC para cada gênero
    if genero == 'h':  # Homem
        if imc < 20:
            print(f'{nome}, você está abaixo do peso normal.')
        elif 20 <= imc < 24.9:
            print(f'{nome}, você está no peso ideal.')
        elif 24.9 <= imc < 29.9:
            print(f'{nome}, você está com obesidade leve.')
        elif 29.9 <= imc < 39.9:
            print(f'{nome}, você está com obesidade moderada.')
        else:
            print(f'{nome}, você está com obesidade mórbida.')

    elif genero == 'm':  # Mulher
        if imc < 19:
            print(f'{nome}, você está abaixo do peso normal.')
        elif 19 <= imc < 23.9:
            print(f'{nome}, você está no peso ideal.')
        elif 23.9 <= imc < 28.9:
            print(f'{nome}, você está com obesidade leve.')
        elif 28.9 <= imc < 38.9:
            print(f'{nome}, você está com obesidade moderada.')
        else:
            print(f'{nome}, você está com obesidade mórbida.')

except ValueError:
    print("Erro: Certifique-se de inserir números válidos para peso e altura.")
