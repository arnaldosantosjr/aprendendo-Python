# Tipo list - Multável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizaveis -indices e fatiamento
# Métodos úteis:
#     appen - Adiciona um item ao final
#     insert - Adiciona um item em um índice específico
#     pop - Remove o último item ou o item do índice específico
#     del - Remove o item do índice específico
#     clear - Limpa a lista
#     extend - Estende a lista com outra lista
#     + - Concatena duas listas
# Create Read Update Delete
# Criar, ler, alterar, apagar = lista[1] (CRUD)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b # Concatena as duas listas
lista_d = lista_a.extend(lista_b) # Estende a lista_a com os valores da lista_b
print(lista_c) # Exibe a lista concatenada
print(lista_d) # None
print(lista_a) # Exibe a lista_a estendida