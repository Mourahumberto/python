# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

caminho_arquivo = 'TESTANDO.txt'

def listar():
    print(lista_completa)
    
def desfazer():
    ultimo = ""
    try:
        ultimo = lista_completa[-1]
        del lista_completa[-1]
        print("Desfazendo")
        lista_refazer.append(ultimo)
        return lista_refazer
    except:
        print("Não existem valores para retirar")

def refazer():
    try:
        ultimo = lista_refazer.pop()
        print(ultimo)
        lista_completa.append(ultimo)
    except:
        print("Não existem valores para colocar")

def adicionar():
    lista_completa.append(digitado)
    print("Adicionando")
    
def salvar():
    with open(caminho_arquivo, 'w') as arquivo:
        for item in lista_completa:
            print(item)
            arquivo.write(f'{item} \n')
        print("Done")

lista_completa = []
lista_refazer =[]
while True:
    print("Comandos: listar, desfazer, refazer e salvar")
    digitado = input("Digite uma tarefa ou comando: ")
    if digitado == "listar" or digitado == "Listar":
        listar()
        
    elif digitado == "desfazer" or digitado == "Desfazer":
        desfazer()
        
        
    elif digitado == "refazer" or digitado == "Refazer":
        refazer()
    
    elif digitado == "salvar":
        salvar()
        
    else:
        adicionar()


