def soma(*args):
    total = 0
    for unidade in args:
        # total = total + unidade
        total += unidade
    print(total)

soma(10,20,30,40,50)
numeros = 1, 2, 3, 4, 5, 6

print(numeros) #empacotados
print(*numeros) #desempacotados