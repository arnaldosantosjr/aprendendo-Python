'''
Faça um progema que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva : "Seu nome é curto."; se tiver entre 5 e 6 letras, escreva: "Seu nome é normal."; Se maior que 6 letras: "Seu nome é grande".'''

nome = input('Infome o seu primeiro nome. \n')
print(len(nome))

if len(nome) <= 4:
    print(f'O nome "{nome}" é muito curto')
elif len(nome) == 6 or len(nome) == 5:
    print(f'O nome "{nome}" é normal ')
else:
    print(f'O nome "{nome}" é grande')