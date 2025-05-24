'''Criando um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome'''
nome = str(input('Qual o seu nome completo?\n'))
print(f'O seu nome completo é:\n {nome}.')
print(f'O seu nome comtodas as letras maiúsculas é: \n{nome.upper()} ')
print(f'O seu nome com todas as letras em minúsculas é: \n{nome.lower()}')
print(f'O seu nome tem {len(nome) - nome.count(' ')} letras no total.')
print(f'O seu nome tem {nome.find(' ')} letras nonprimeiro nome.')
