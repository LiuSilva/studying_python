# 111: Crie um script com um dicionário, ao qual vai ter no seu valor uma lista para cada pessoa,
# com as linguagens que ele gosta, faça um loop for, para mostrar o nome da pessoa com uma mensagem,
# ex: 'rodrigo sua linguagem preferida e' ...
# em seguida faça um segundo loop dentro do 1, que mostre as linguagens que estão na lista use .items() explique.

pessoas = {
    'Luiza': ['Python', 'C#'],
    'Rodrigo': ['C', 'ShellScript', 'Python', 'HTML', 'JavaScript'],
    'Luiz': ['C++', 'Java', 'Python', 'Ruby', 'PHP', 'HTML'],
    'Greicy': ['Java', 'Python', 'Lua']
}

for pessoa, linguagens in pessoas.items():
    print(pessoa.title(), 'você gosta das linguagens de programação:')

    for linguagem in linguagens:
        print('\t'*12, linguagem)

