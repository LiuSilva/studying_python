# 94: Crie um script com um dicionário vazio e adicione chaves com seus valores.

dicionario = {}

keys = ['nome', 'idade', 'telefone', 'email', 'endereco']
values = ['Harry Potter', '25', '(00) 9 9999-8888', 'hpotter@gmail.com', 'Rua dos Alfeneiros nº 4']

for i in range(0, 5):
    dicionario[keys[i]] = values[i]

print(dicionario)
