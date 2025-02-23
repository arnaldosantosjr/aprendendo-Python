# Precedência entre os operadores
#1. (n + n)
#2. **
#3. * 3 / // %
#4. + - 
conta_1 = 1 + 1 ** 5 + 5
conta_2 = (1 + 1) ** 5 + 5
conta_3 = (1 + 1) ** (5 + 5)
print(conta_1) #7
print(conta_2) #37
print(conta_3) #1024
