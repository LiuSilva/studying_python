# 92:Crie um script com um dicionário e adicione uma pessoa com uma pontuação,
# Depois crie uma variável armazene o valor da chave a ela,
# print uma mensagem concatenando com a variável que fale quantos pontos a pessoa tem.

person = {'name'  : "Jon Snow",
          'skill' : 'Guerreiro',
          'score' : '88'}

nome = person['name']

pontos = person['score']

print(nome.title() + ", você conseguiu", pontos, "pontos matando o White Walker!")