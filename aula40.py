"""Calculadora com While"""
while True:
    num1 = input('Digite um múmero: ')
    num2 = input('Digite outro número: ')
    oper = input('Digite o operador (+ - / *): ')

    numeros_validos = None

    try:
        num1_float = float(num1)
        mum2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os numoreos são invalidos')
        continue
    
    operadores_permitidos = '+-/*'

    if oper not in operadores_permitidos:
        print('Operador invalod')

    if len(oper) >1:
        print('Digite apenas um operador.')
        continue

    sair = input('Que sair [S]im: ').lower().startswith('s')
    
    if sair is True:
        break