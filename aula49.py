# Lista em Python
# Tipo de list - Mutável
# Suporta vários valores de  qualquer tipo
# Conhecimentos reutilizáveis - indice e fatiamento
# Métodos úteis: 
#      append, insert, pop, del, clear, extend, +
# Crate REand Update   Delete
# Criar, ler, alterar, apagar = lista[1] (CRUD)
# del - remove o elemento da lista
# pop - Remove o final ou o indice escolhido
# clear - Limpa a lista
# extend - Estende a lista
# + - Concatena duas listas


#         0  1  2  3  
lista = [10,20,30,40]
# lista[2] = 300

# print(lista) 
# print(lista[2]) # Exibe o valor do índice 2 da lista
# del lista[2] # Remove o elemento do índice 2 da lista
# print(lista) # Exibe a lista após a remoção do elemento

lista.append(50) # Adiciona o valor 50 ao final da lista
lista.pop()
lista.append(60) # Adiciona o valor 60 ao final da lista
lista.append(70) # Adiciona o valor 70 ao final da lista
lista.pop()
ultimo_valor = lista.pop(3)
del lista[0] # Remove o elemento do índice 0 da listaina
lista.insert(0, 'Arnaldo') # Adiciona o valor 'Arnaldo' no índice 0 da lista
print(lista, 'Removido', ultimo_valor) # Exibe a lista após adicionar os elementos
