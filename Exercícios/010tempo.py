'''Convertendo o valor para o formato horas:minutos:segundos (00:00:00)'''
N = int(input('Informe o valor a ser convertido.\n'))
horas = N // 3600
resto = N % 3600
minutos = resto // 60
segundos = resto % 60

print(f'{horas}:{minutos}:{segundos}')