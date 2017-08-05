# 108: Desafio extra: crie um script com uma lista vazia,faça um loop for com um range de 30,
# faça uma variável para receber o dicionario, nele vai ter, cor,pontos e velocidade com seus valores,
# adicione os valores na lista vazia,faça um novo loop que mostre apenas 5 dicionários,
# por ultimo print quantos dicionários tem na sua lista use (range() for fatiamento[:5] len() ) explique.

personagens = []

for i in range(30):
    personagens.append({'nome':'jedi['+str(i)+']', 'cor': 'verde', 'pontos': 80, 'velocidade': 'Rapido'})

for i in range(150):
    personagens.append({'nome':'clone', 'cor': 'branco', 'pontos': 50, 'velocidade': 'Lento'})

for personagem in personagens[:5]:
    print(personagem)

print("Total de personagens=", len(personagens))