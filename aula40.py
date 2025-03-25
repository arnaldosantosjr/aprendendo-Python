"""Calculadora com While"""
while True:
    num1 = input('Digite um múmero: ')
    num2 = input('Digite outro número: ')
    oper = input('Digite o operador (+ - / *): ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
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
    print('Realizando a sua conta')
    if oper =='+':
        print(f'{num1_float + num2_float} = ', num1_float + num2_float)

    elif oper =='-':
        print(f'{num1_float - num2_float} = ', num1_float - num2_float)

    elif oper =='/':
        print(f'{num1_float / num2_float} = ', num1_float / num2_float)

    elif oper =='*':
        print(f'{num1_float * num2_float} = ', num1_float * num2_float)

    else:
        print('Não deveria chegar aqui!')

    sair = input('Que sair [S]im: ').lower().startswith('s')
    
    if sair is True:
        break