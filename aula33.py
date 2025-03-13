'''
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str:, int, float, bool
'''
string = 'arnaldo Leão'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
#string[3]= 'ABC'
print(string[3])
print(outra_variavel)
print(string.capitalize())#Torna aprimeira letra Maiúscula se ela estiver minúscula 
print(string.zfill(50)) #preence a esquera com a quantidade determinada de zeros