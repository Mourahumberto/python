import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def func_que_roda_funcao():
        print("*************** Embrulhando a função decoradora***********")
        funcao()
        print("************ Depoiis de embrular a função*****************")
    return func_que_roda_funcao

@meu_decorador
def minha_funcao():
    print("Eu sou a função")
    

minha_funcao()
