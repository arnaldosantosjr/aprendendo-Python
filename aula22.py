# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer das condoções verdadeira avalia
# tods a expressão como verdade
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor
# São considerados falsy
# 0.0.0. ''  Fale 
# também existe o tipo None que é 
# usado para representar um não valor

'''
entrada = input('[E]ntrar [S]air\n => ')
senha_digitada = input ('Senha: ')


senha_premitida = '123456'
# if True:

#if condicao:
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_premitida:
    print('Entrar')
else:
    print('Sair')




# Avaliação de curto circuito
print(True or False or 0)
print(True or False or 'abc')
print(0 or False or 'abc')
'''
senha = input('Senha: ') or 'Sem senha'
print(senha)