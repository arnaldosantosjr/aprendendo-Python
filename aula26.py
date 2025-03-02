'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígito>f
x ou X Hexadecimal
(Cractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - força o número aparecer antes dos zeros
Sinal + ou -
Ex.: 0> -100, .f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:$^10}')
print(f'{variavel:0^10}')
print(f'{1000.1232244355668909:.1f}')
print(f'{1000.1232244355668909:,.1f}')
print(f'{-1000.1232244355668909:+,.1f}')
print(f'{1000.1232244355668909:+,.1f}')
print(f'{1000.1232244355668909:0>+10,.1f}')
print(f'{1000.1232244355668909:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')