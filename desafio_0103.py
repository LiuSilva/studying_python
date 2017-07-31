# 103: Crie um script se a pessoa não estiver no dicionario, print uma mensagem a interrogando,
# exemplo: 'rodrigo você sabe programar ?' use (if, keys()) explique.

linguagens_programacao = {
    'Pedro' : 'JavaScript',
    'Joao': 'PHP',
    'Antonio': 'HTML/CSS',
    'Maria': 'Java',
    'Luiza': 'Python'
}

pessoas = ['Luiza', 'Maria', 'Timoteo', 'Ana', 'Marcos']
for pessoa in pessoas:
    if pessoa in linguagens_programacao.keys():
        print(pessoa, "você gosta de programar na linguagem", linguagens_programacao[pessoa])
    else:
        print(pessoa, "você deveria aprender a programar, é muito divertido!")