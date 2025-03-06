"""
Falag (Bandeira) - Marcar um local
None = Não valor
Is e is not = é ou não é (tipo, valor. identidade)
id = Identidade
"""
condicao = False
passou_no_if = True
if condicao:
    
    print('Faça algo')
else:
    passou_no_if = None
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)