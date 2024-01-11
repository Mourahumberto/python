# os jogadores aqui não são objetos e sim dicionários
jogador_loteria_1 = {
    'nome': 'Pedro',
    'numeros': (1,23,4,56,78,99)
    
}

jogador_loteria_2 = {
    'nome': 'Pedro',
    'numeros': (1,23,4,56,78,99)
    
}

print(jogador_loteria_1 == jogador_loteria_2)

# Classe é um modelo ou uma representação de um objeto (uma forma)
# Objeto é uma instância de uma classe (um bolo)
# Classes podem ter funções dentro dela.

class JogadorLoteria:
    def __init__(self):
        self.nome = "Neto"
        self.numeros = (1,23,4,56,78,99)
    
    def total(self):
        return sum(self.numeros)
    
jogador1 = JogadorLoteria()
jogador2 = JogadorLoteria()
print(jogador2 == jogador1)
print(jogador1)
print(jogador2)
print(jogador1.total())

class JogadorComAtributos:
    def __init__(self,nome):
        self.nome = nome
        self.numeros = (1,23,4,56,78,99)
    
    def total(self):
        return sum(self.numeros)

jogador3 = JogadorComAtributos("Humberto")
print(jogador3.nome)