def generator(n=0):
    yield 1
    print("Continuando1")
    yield 2
    print("Continuando2")
    yield 3
    print("Continuando3")
    yield 4
    print("Continuando4")
    return "ACABOU"
    

gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Vai trazer o return com um erro
#print(next(gen))

# automatizando

def generator2(n=0, maximum=10):
    while True:
        yield n
        n += 1


        if n >= maximum:
            return


gen = generator2(maximum=10)
for n in gen:
    print(n)