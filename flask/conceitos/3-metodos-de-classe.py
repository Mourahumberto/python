import datetime
minha_data = datetime.date(2023, 6, 26)
class Funcionario():
    aumento = 1.04
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def dados(self):
        return {'nome': self.nome, 'salario': self.salario}
    
    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento
    
    # Não depende do objeto e sim da clase.
    @classmethod
    def aplicar_novo_aumento(cls, novo_aumento):
        cls.aumento = novo_aumento
    
    #Não necessita de nem um argumento do objeto por isso não tem self
    @staticmethod
    def dia_util(dia):
        # segunda = 0
        # domingo = 6
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True
        
        
        
fabio = Funcionario('Fabio', 7000)
print(fabio.dados())
Funcionario.aplicar_novo_aumento(1.05)
fabio.aplicar_aumento()
print(fabio.dados())

print(fabio.dados())

print(Funcionario.dia_util(minha_data))
