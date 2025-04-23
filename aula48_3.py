# Cuidaddos com dados mutáveis
# = - copiado o valor (imutáveis)
# = - aponta para o mesmo valor na memória (mutáveis)


nome = 'Arnaldo'
nourtra_variavel = nome # Copia o valor de 'Arnaldo' para outra_variavel
nome = 'Tony'
print(nome) # Exibe 'Tony' (substitui o valor anterior)
print(nourtra_variavel) # Exibe 'Arnaldo' (valor copiado)
lista_a = ['Tony', 'Arnaldo',1, True, 1.2]
#lista_b = lista_a
lista_b = lista_a.copy() # Copia os valores da lista_a para a lista_b
 
lista_a[0] = 'Qualquer coisa' # Altera o valor do índice 0 da lista_a
print(lista_a) # Exibe 'Qualquer coisa' (substitui o valor anterior) 
print(lista_b) # Exibe 'Qualquer coisa' (aponta para o mesmo valor na memória)