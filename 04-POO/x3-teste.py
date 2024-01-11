class Carro:
    def __init__(self, nome, n_portas):
        self.nome = nome
        self.n_portas = n_portas
        self._motor = None
        self._fabricante = None
        self._pneu = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    @property
    def pneu(self):
        return self._pneu
    
    @pneu.setter
    def pneu(self, valor):
        self._pneu = valor
        
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
  

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Pneu:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca', '2 Portas')
volkswagen = Fabricante('volkswagen')
fusca.fabricante = volkswagen
motor_1_0 = Motor('1.0')
fusca.motor = motor_1_0
bridgestone = Pneu('Bridgestone')
fusca.pneu = bridgestone
print(fusca.nome, fusca.n_portas, fusca.motor.nome, fusca.fabricante.nome, fusca.pneu.nome)