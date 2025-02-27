# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condoções precisam ser satisfeitas
# verdade
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy
# 0.0.0. ''  Fale 
# também existe o tipo None que é 
# usado para representar um não valor

#entrada = input('[E]ntrar [S]air\n => ')
#senha_digitada = input ('Senha: ')


#senha_premitida = '123456'
# if True:

#if condição:
#if entrada == 'E' and senha_digitada == senha_premitida:
#    print('Entrar')
#else:
#    print('Sair')




# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
print(True and 1 and True)
print(bool (''))