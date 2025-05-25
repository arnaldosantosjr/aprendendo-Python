'''
Este projeto é uma calculadora de imc mais precisa
Ela calcula o imc também de acordo com o gênero do usuário
'''
import tkinter as tk
from tkinter import messagebox
while True:
    genero = input('Qual o seu gênero?\nDigite [H]omem ou [M]ulher:\n').strip().lower() #stripe verifica se há espaço e lower ajusta para que não haja problemas entre letras maiúsculas e minúsculas
    if not genero or genero not in ['h', 'm']:
        print('GÊNERO INVALIDO!!!!')    
    else: 
        break

nome = input('Qual o seu nome?\n').strip()

while True:
    try:
        peso = float(input('Qual o seu peso em Kg?\n').strip())
        altura = float(input('Digite sua altura em m.\n').strip())
        if peso > 0 and altura> 0:
            imc = peso / (altura ** 2)
            print(f'{nome}, o seu imc é:{imc:.2f}')
            break
        else:
            print('O peso e altura devem ser diferentes de zero')
    except ValueError:
        print('Erro: Insira valores válidos para peso e altura')

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


    