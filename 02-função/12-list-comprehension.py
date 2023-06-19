# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
    print(lista)

print()
lista = [numero for numero in range(10)]
print(lista)

print()

#List comprehension 
lista = [
    numero*2 for numero in range(10)
    ]
print(lista)

# Mapeamento de dados em list comprehension 

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')

# Filtro em list comprehension 

lista1 = list(range(10))
lista2 = [
    item for item in lista1 if item > 5
]

print(lista2)

produtos_mais_caros = [
    # {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos
    {**produto} for produto in produtos if produto['preco'] > 10
]

print(*produtos_mais_caros, sep='\n')