'''
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
obs.: a função len retorna a qtd
de carateres da str
'''
variavel ='Olá mundo'
print(variavel[5])
print(variavel[4:])
print(variavel[4:7])#O final não é incluido
print(variavel[4:8])#coloca um indice a mais para pegar o final
print(variavel[0:4])
print(variavel[:5])
print(variavel[-8:-2])
print(len(variavel[-8:-2])) #6
print(len(variavel)) #9
print(variavel[0:len(variavel):1]) 
print(variavel[0:9:1]) 
print(variavel[0:9:3]) 
print(variavel[0:9:2]) 
print(variavel[-1:-10:-1]) 


