# Opreador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input ('Senha: ')

#forma que costumamos fazer
'''
if senha == '123456':
    print ('Enteou')
else:
    print ('Senha incorreta. ')

    '''
# forma com negação:
# Seria a mais adequanda para a amioria dos casos 
# Verifica primeiro se a Senha corresponde
'''
if senha != '123456':
    print('Senha incorreta!')
'''
if not senha:
    print('preencha o campo da senha!')
