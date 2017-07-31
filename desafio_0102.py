# 102: Crie um script com o loop for, que mostre o nome da pessoa e sua linguagem favorita,
# apenas se ela estiver na sua lista use ( keys() if ) explique.

linguagens_programacao = {
    'Pessoa1' : 'JavaScript',
    'Pessoa2': 'PHP',
    'Pessoa3': 'HTML/CSS',
    'Pessoa4': 'Java',
    'Pessoa5': 'Python'
}

pessoas = ['Pessoa5', 'Pessoa4', 'Pessoa6']
for chave in linguagens_programacao.keys():
    if chave in pessoas:
        print(chave, "você gosta de programar na linguagem", linguagens_programacao[chave])