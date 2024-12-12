texto = 'Python'

# jeito mais simples de iterar, com um iterável que tem final.
# continue e break são usados no for da mesma forma.
for letra in texto:
    print(letra)
    
for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue
  
    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print('For completo com sucesso!')

# for com listas
lista = ['Maria', 'Helena', 'Luiz']

indice = 0
for nome in lista:
    indice +=1
    print(indice ,nome)
