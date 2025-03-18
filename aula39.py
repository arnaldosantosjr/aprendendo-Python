'''
Iterando string com while
'''
       #0123456789101112...
nome = 'Arnaldo Leão' #iteraivis

#nova_string += '*A*r*n*a*l*d*o* *S*a*n*t*o*s'

indice = 0
novo_nome = ''
while indice < len(nome):
       letra = nome[indice]
       
       novo_nome += f'*{letra}'
       indice += 1
       
novo_nome +='*'
print(novo_nome)

       