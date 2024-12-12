"""
Introdução às funções (def) em Python
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def imprimir1(a, b, c):
    print(a, b, c)


def imprimir2(a, b, c):
    print(a, b, c)
    return "testando"

teste1 = imprimir1(1,2,3)
teste2 = imprimir2(3,2,1)
teste3 = imprimir2(c=3,b=2,a=1) #argumentos nomeados

print(teste1, teste2, teste3)

####################################################################
def saudacao(nome='Sem nome'): # colocando argumentos com default
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao() # vem o valor default

