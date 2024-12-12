pessoa = {
    'nome' : 'Neto',
    'sobrenome': 'Moura',

}

dados_pessoa = {
    'idade': 20,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
pessoa_completa2 = {**pessoa, 'nome':"Humberto"}
print(pessoa_completa)
print(pessoa_completa2)


def mostro_argumentos_nomeados(*args, **kwargs):
    # Vai imprimir coisas não nomeados
    print(args)
    #vai printar argumentos chaves valor
    print(kwargs)
    #aqui vai trazer os itens dos kwargs
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados("teste", 123, nome="May", qlq=123)
# passou desempacotado para a função
mostro_argumentos_nomeados(**pessoa_completa)