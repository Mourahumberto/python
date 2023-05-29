"""
Retorno de valores das funções (return)
"""


def operacao(x, y):
    if x > 10:
        return x - y
    return x + y


# variavel = soma(1, 2)
# variavel = int('1')
operacao1 = operacao(2, 2)
operacao2 = operacao(3, 3)
print(operacao1)
print(operacao2)
print(operacao(11, 55))