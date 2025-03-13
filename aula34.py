'''
Repetições
while (enquanto)
Executar uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando não tem fim

Ex:
condicao = True

while condicao:
    print(1)
    print(2)
    print(3)
'''
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break #Serve para buscar um while mais proximo e quando atingido sai do laço

print('Acabou')