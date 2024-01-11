class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}
    
fabio = Funcionario('Fabio', 1600)
print(fabio.dados())

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados
    
fernando = Admin('fernando', 2000)
print(fernando.dados())
fernando.atualizar_dados('Neto')
print(fernando.dados())
