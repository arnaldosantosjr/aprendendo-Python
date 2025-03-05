'''
Exercício
Peça ao  usuário para digitar seu nome
Peça para o usuário digitar sua idade
Se o valor digitado na idade não for inteiro imprima: valor para idade é iválido
Se nome e idade forem digitados:
    exiba:
        Seu nome é: (nome)
        Seu nome invertido é {nome invertido}
        Seu nome contem  (ou não) espaços
        Seu nome tem {n} letras
        primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios
'''
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
'''try:
    print('SRT:', idade')
except:'''

if idade and nome != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome tem {len(nome)}, letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
    if ' ' in nome:
        print(f'Há espaço em: {nome}')
    else:
        print(f'Não há espaço em: {nome}')
else:
    print('Desculpe, você deixou campos vazios.')