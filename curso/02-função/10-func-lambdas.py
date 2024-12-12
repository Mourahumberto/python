# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

#Transformando funções em lambdas


preco = 0

def calcular_imposto(preco):
    return preco*0.3
print(calcular_imposto(1000))

# transformando pra lambda

calcular_imposto2 = lambda x: x*0.3

print(calcular_imposto2(1000))

precos = [10,20,30,40]
calcular_imposto3 = list(map(lambda x: x*0.3, precos))
print(calcular_imposto3)