'''
Interável -> str, range, etc.(__iter__)
Interior -> quem sabe entregrar um valor por vez
next -> me entregue o próximo valor
iter -> me me entregue seu interador
'''
texto ='Arnaldo' #iteravel
# iteratador = iter(texto) #iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break   

for letra in texto:
    print(letra)