# 105: Crie um script com um dicionario, faça um loop for,
# que apenas mostre os valores das chaves use .values() explique

linguagens_programacao = {
    'Pedro' : 'JavaScript',
    'Joao': 'PHP',
    'Lucas': "Python",
    'Antonio': 'HTML/CSS',
    'Maria': 'Java',
    'Luiza': 'Python'
}

for linguagem in linguagens_programacao.values():
    print(linguagem)

'''
O metodo .values() retorna todos os valores contidos no dicionário
'''