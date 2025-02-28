'''
interpolação básica de string com % em python
s - string
d e i - int
f - float
x e X hexadecimal (ABCDEF0123456789)
'''
nome = 'Arnaldo'
preco = 100.95897643
variavel = '%s, o preço total é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X'%(15, 15))