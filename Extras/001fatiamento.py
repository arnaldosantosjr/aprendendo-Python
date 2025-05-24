#Fatiamento, análise, divisão, junição de strings
frase ='Curso em Vídeo Python'
frase2 = '   Apreenda Python  '
print(frase[:5])
print(frase[5])
print(frase[5:])
print(frase[::2])
print(frase[9::3])
print(frase[::])
print(frase[5:10:2])
print(len(frase))#Quantidade de caracteres
print(frase.count('o'))#Contar quantas vezes aparece a letra 'o'
print(frase.count('o', 0, 13))#Contar quantas vezes aparece a letra 'o' entre o índice 0 e 13
print(frase.find('deo'))#Encontrar a posição da string 'deo' (em que posição começa)
print(frase.find('Android'))#Retorna -1 se não encontrar
print('Curso' in frase)#Verifica se a string 'Curso' está contida na variável frase (True ou False)
print(frase.replace('Python', 'Android'))#Substitui a string 'Python' por 'Android'(replece é o mesmo que trocar)
print(frase.upper())#Coloca tudo em maiúsculo
print(frase.lower())#Coloca tudo em minúsculo
print(frase.capitalize())#Coloca a primeira letra em maiúsculo
print(frase.title())#Coloca a primeira letra de cada palavra em maiúsculo
print(frase2)
print(frase2.strip())#Remove os espaços em branco do início e do fim da string
print(frase2.rstrip())#Remove os espaços em branco do fim da string
print(frase2.lstrip())#Remove os espaços em branco do início da string
print(frase.split())#Divide a string em uma lista de palavras
print('-'.join(frase))
