# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

count = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    for opcao in pergunta['Opções']:
        print(opcao)
    r = input("qual a resposta? ")
    if r == pergunta['Resposta']:
        print("Muito bem")
        count += 1
    else:
        print("erroou")
print(count)