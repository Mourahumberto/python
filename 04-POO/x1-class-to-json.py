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

p1 = Pessoa("Humberto", 29)
p2 = Pessoa("Mayara", 28)
p3 = Pessoa("Nicole", 5)
dados_pessoas=[vars(p1), vars(p2), vars(p3)]

with open (CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(
        dados_pessoas,
        arquivo,
        ensure_ascii=False,
        indent=2)