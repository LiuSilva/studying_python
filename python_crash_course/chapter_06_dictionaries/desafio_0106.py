# 106: Faça como o 105, porem o dicionário  vai ter um valor repetido na chave,
# então faça mostrar o valor apenas uma vez, caso ele apareça mais de uma, use values() set()

linguagens_programacao = {
    'Pedro' : 'JavaScript',
    'Joao': 'PHP',
    'Lucas': "Python",
    'Antonio': 'HTML/CSS',
    'Maria': 'Java',
    'Luiza': 'Python'
}

for linguagem in set(linguagens_programacao.values()):
    print(linguagem)

'''
O metodo .set() remove as duplicatas da lista gerada pelo .values(), criando assim uma lista sem duplicatas
no seu conteudo, se não usar o set(), os valores duplicados serão mostrados
'''