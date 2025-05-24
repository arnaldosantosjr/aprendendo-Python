'''Este programa ler o nome de um cidade  e verifica se ela começa com a palavra "Santo".'''
cidade = str(input('Digite o nome da sua cidade📍: \n'))
print(f'O nome da sua cidade é: {cidade} ')
if cidade[:5].upper() == 'SANTO':

    print('A sua cidade começa com a palavra "Santo".')
else:
    print('A sua cidade não começa com a palavra "Santo".')