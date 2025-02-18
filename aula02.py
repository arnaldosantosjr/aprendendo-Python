#\r \n ->CRLF  (Faz com que o computador quebre a linha)

print(12, 34, sep=' ', end='\r\n')#Quebra  alinha


print(56, 78, sep=" ", end='##')#Não quebra  alinha

'''
Neste caso, o que fica dentro das ápas, é o que separa.
##\n Insere as duas cerquilhas e quebra  alinha.
'''
print(90, 12, 23, sep=' recomeço ', end='## \n') 
