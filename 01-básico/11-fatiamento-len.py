"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
print(variavel[2])
print(variavel[3:])
print(variavel[:2])
print(variavel[2:5])
print(variavel[::2])

# Com string ele conta o número de carcteres na string
print(len(variavel))