# Formatação de strings com método format

a = 'A'
b = 'B'
c = 1.1
string =  'a = {nome1} b = {nome2} c = {nome3:.2f}' # Também é ´psssivel fazer colocando os índides: 'a = {0} b = {1} c = {2:.2f}', a vantagem é que não precisa se preocupar com a ordem, mas índices podem não ser confiáveis
formato = string.format(
    nome1=a, nome2=b, nome3=c)

print(formato)

#Quando uma função está dentro de um um objeto ela é chamad de método
#Tudo em python é um objeto