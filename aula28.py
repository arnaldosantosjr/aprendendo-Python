'''
Exercício
Peça ao  usuário para digitar seu nome
Peça para o usuário digitar sua idade
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
nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade:'))

if nome or idade != '':
    print(f'Seu nome é {nome}')
    print(f'sua idade é {idade}')
    print(f'Seu nome ao contrário é: {nome [::-1]}')# inverter a escrita
    if ' ' in nome : # Verifivcando se há espaços no nome
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem :{len(nome)} letras.') # quantidade de letras 
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')

else:
    print('você deixou campos vazios')
