# 93: Crie um script com um dicionário que tenha um personagem com 2 valores em suas chaves :
# em seguida adicione mais 2 valores ao dicionário explique.

person = {'name'  : "Jon Snow",
          'skill' : 'Guerreiro',
          'score' : '88'}

person['girlfriend'] = "Ygritte"
person['pet'] = "Giant Wolf Ghost"

nome = person['name']

pontos = person['score']

print(nome.title() + ", você conseguiu", pontos, "pontos matando o White Walker!")

print(person['girlfriend'].title() + " says \"You know nothing", nome + "\"")
