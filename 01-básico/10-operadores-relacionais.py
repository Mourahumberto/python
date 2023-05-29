"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print('Olha meu print aqui')

"""
Operadores lógicos
and (e) or (ou) not (não)
or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
and - Necessita que toda as condições sejam verdadeiras para que a saída seja verdadeira.
Também existe o tipo None que é usado para representar um não valor
valores considerados falsos 0 0.0 '' False
#not True = false
#not False = True
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)

# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
nome = 'Otávio'
print(nome[2])
print(nome[-4])
print('vio' in nome)
print('zero' in nome)

print('vio' not in nome)
print('zero' not in nome)