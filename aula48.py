# Lista em Python
# Tipo de list - Mutável
# Suporta vários valores de  qualquer tipo
# Conhecimentos reutilizáveis - indice e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +

#       01234
#       -54321
string = 'ABCDE' # 5 caracteres (len)
# uso os couchetes para acessar os elementos da string ou da lista
#lista = []
# lista = list()# Converte a string em uma lista de caracteres
# print(lista) # Exibe a lista vazia

# print(lista, type(lista)) # Exibe a lista vazia também
#print(bool(list)) # Exibe False, pois a lista está vazia

#        0     1       2       3    4
#       -5    -4      -3      -2   -1
lista = [123, True,'Arnaldo', 1.2, [] ]
lista[2] = 'Tony' # Altera o valor do índice 2 da lista
print(lista[2].upper(), type(lista[2]))# Exibe 'TONY' (converte para maiúsculas)