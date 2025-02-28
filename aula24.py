# Opreador in e not in
# in siginifica entre e not in significa não entre
# String são interáveis
# 0 1 2 3 4 5 6
# A r n a l d o
#-7-6-5-4-3-2-1

'''
nome = 'Arnaldo'
print (nome[2])
print (nome[-4])

# checando se uma letra está na string

print('a' in nome)
print('z'in nome)

# fazendo o inverso

print('a' not in nome)
print('z' not in nome)

'''

nome = input ('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print (f'{encontrar} etá em nome')

else: 
    print(f'{encontrar} não está em nome.')