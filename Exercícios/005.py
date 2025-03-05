nome = input('Qual o seu nome?\n')
peso = input('Qual o seu peso?\n')
altura = input('Digite sua altura\n')

#converti os valores do peso e da altura, que estavam como str para float
float_peso = float(peso)
float_altura = float(altura)
imc = float_peso / float_altura ** 2

print(f'{nome}, O seu imc é:{imc:.2f}')