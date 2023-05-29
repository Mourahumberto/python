Nome = "Humberto Moura"
n_nome = len(Nome)
contador = 0
novo_nome = ""
while contador < n_nome:
    print(Nome[contador])
    novo_nome += "*" + Nome[contador]
    contador += 1
print(novo_nome)