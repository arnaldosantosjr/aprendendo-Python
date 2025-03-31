frase = 'O Python é uma linguagem de programação'\
    'multiparadigma.'\
    'Python foi criado por Guido van Rossum'

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    apareceu_mais_vezes_atual = frase.count(letra_atual)

    if apareceu_mais_vezes < apareceu_mais_vezes_atual:
        apareceu_mais_vezes = apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1   
print('A letra que apaeceu mais vezes foi a letra '
    f'"{letra_apareceu_mais_vezes}", que apareceu'
    f' {apareceu_mais_vezes}x')
   