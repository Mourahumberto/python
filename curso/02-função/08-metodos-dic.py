# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# Cópias em dicionários.
# QUANDO VOCÊ COPIA VALORES MUTÁVEIS, ELES APONTAM PARA O MESMO PONTEIRO NA MEMÓRIA

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}

d2 = d1 
print(d1)

d2['c1'] = 1000
print(d1)

## COPY copia os valores imutáveis e os mutáveis ele cria um link pro ponteira

d3 = copy.copy(d1)
print()
print(d1)
print(d3)
d3['c1'] = 9999
d3['l1'][1] = 88888
print()
print(d1)
print(d3)

## copia tudo de fato, sem fazer nem um apontamento.
d4 = copy.deepcopy(d1)
print()


d4['c1'] = 9999
d4['l1'][1] = 77777
print()
print(d1)
print(d4)
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

print(p1['nome'])
print(p1.get('nome', 'Não existe'))

nome = p1.pop('nome')
print(nome)
print(p1)
print()

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)
p1.update({
    'nome': 'novo valor',
    'idade': 30,
})
p1.update(nome='novo valor', idade=30)
tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)