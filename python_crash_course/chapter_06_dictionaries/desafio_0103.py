# 103: Crie um script se a pessoa não estiver no dicionario, print uma mensagem a interrogando,
# exemplo: 'rodrigo você sabe programar ?' use (if, keys()) explique.

linguagens_programacao = {
    'Pedro' : 'JavaScript',
    'Joao': 'PHP',
    'Antonio': 'HTML/CSS',
    'Maria': 'Java',
    'Luiza': 'Python'
}

if "Lourenço" not in linguagens_programacao.keys():
    print("Lourenço você deveria aprender a programar, é muito divertido!")