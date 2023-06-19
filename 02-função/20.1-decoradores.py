def func(f):
    def wrapper(x):
        print("Iniciada")
        f(x)
        print("Finalizada")
    return wrapper
@func
def f1(x):
    print(f"O valor de x é = {x}")
@func
def f2():
    print("Função f2() chamada")