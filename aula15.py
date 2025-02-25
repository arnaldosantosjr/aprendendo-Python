#Usando a função input para coletar dados

#nome = input('Qual o seu nom? ')

#print(f'O seu nome é {nome}')
#print(f'O seu nome é {nome =}') #É útil para que eu possa ver o valor da variável 

#Forma mais comum e não mais adequada de se trabalhr com o input

'''numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))'''


#Forma mais adequanda , meso senfo  amis longa.
#Aqui impede que haja uma quebra no código
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')