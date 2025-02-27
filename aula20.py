primeiro_valor = input('digite um valor: ')
segundo_valor = input('Digite outro valor: ')


if primeiro_valor > segundo_valor:
    print(f'O primeiro valor é = {primeiro_valor}, é maior que o segundo valor ={segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'O segundo valor = {segundo_valor}, é maior que o primeiro valor = {primeiro_valor}')
else:
    print(f'Os dois valore são igais: {primeiro_valor} = {segundo_valor}')