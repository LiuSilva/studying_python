# 95: Crie um script com um dicionário e um personagem ele vai ter um valor na chave, vai ser uma cor ,
# em seguida altere a cor, faça duas mensagens para antes e depois alterar a cor,
# exemplo , ’ cor do personagem e  vermelho ‘  ‘a cor do personagem agora e  preto’ explique.

dicionario = {}

keys = ['nome', 'idade', 'telefone', 'email', 'endereco']
values = ['Harry Potter', '25', '(00) 9 9999-8888', 'hpotter@gmail.com', 'Rua dos Alfeneiros nº 4']

for i in range(0, 5):
    dicionario[keys[i]] = values[i]

dicionario['cor'] = "verde"

print(dicionario['nome'].title(), "sua cor é", dicionario['cor'])

dicionario['cor'] = "vermelho"

print(dicionario['nome'].title(), "sua nova cor é", dicionario['cor'])