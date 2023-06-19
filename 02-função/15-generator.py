import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
# ele salva tudo isso em memória, ocupa mais espaço na memória. porém você consegue acessar indices
lista = [n for n in range(1000000)]
# Mais leve ocupa menos espaço na memória, porém so conhece o próximo valor, não consegue acessa indices.
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

for n in generator:
    print(n)