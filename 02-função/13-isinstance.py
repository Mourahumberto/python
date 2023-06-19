# isinstace - para saber se objeto é de determinado tipo
lista = [
    'neto', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, str):
        teste = item.upper()
        print(teste)
        
    if isinstance(item, list):
        item.append(6)
        print(item)