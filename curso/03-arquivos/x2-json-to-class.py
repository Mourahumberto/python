# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = "teste1.json"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
with open (CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)

for pessoinha in pessoas:
    p1 = Pessoa(**pessoinha)
    print(p1.nome)

