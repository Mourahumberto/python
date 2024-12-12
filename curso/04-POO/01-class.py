# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    ano_atual = 2022
    def __init__(self, nome="fulano", sobrenome="ciclano"):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar(self, amigo):
        return f'{self.nome} fala oi para o {amigo} no ano de {Pessoa.ano_atual}'

    
p1 = Pessoa('Humberto', 'Moura')
p2 = Pessoa()
print(p1.nome)
print(p2.nome)
print(type(p1))
print(p1.falar("Mayara"))
print(p1.ano_atual)

