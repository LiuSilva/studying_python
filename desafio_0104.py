# 104: Crie um script com o loop for, que mostre cada pessoa no seu dicionario,
# com uma mensagem para cada pessoa de forma ordenada, use sorted() keys() explique.

linguagens_programacao = {
    'Pedro' : 'JavaScript',
    'Joao': 'PHP',
    'Antonio': 'HTML/CSS',
    'Maria': 'Java',
    'Luiza': 'Python'
}

for pessoa in sorted(linguagens_programacao.keys()):
    print(pessoa)