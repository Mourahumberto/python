"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [123, "humberto", True, 1.2]
print(lista)

lista = [10, 20, 30, 40, 50, 60, 70]
print(lista)
lista[2] = 300
print(lista)
del lista[4]
print(lista)
lista.append(80)
print(lista)
lista.pop(3)
print(lista)
lista.insert(2, "neto")
print(lista)
print(lista[-1])

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_a)
lista_a.extend(lista_b) # faz a ação no lista_a
print(lista_c)
print(lista_a)