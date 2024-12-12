# (Parte1) try e except para tratar exceções

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error: # o as indica em qual variável quer salvar a instância do erro
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Name:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')
finally:
    print('SEMPRE SERÁ EXECUTADO') #Independente de dar erro ou não o finally sempre será executado, é importante pra fechar conexão com o banco de dados ou algo do tipo.

print('CONTINUAR')