# 109: Faça semelhante ao 108, porem altere os 3 primeiros valores dos dicionários
# cor, pontos, e velocidade, depois mostre o resultado com os dicionários alterados
# use range() fatiamento [:] if explique.

personagens = []

for i in range(30):
    personagens.append({'nome':'jedi['+str(i)+']', 'cor': 'verde', 'pontos': 80, 'velocidade': 'Rapido'})

for personagem in personagens[:3]:
    personagem['nome'] = 'padawan'
    personagem['pontos'] = 20
    personagem['velocidade'] = 'Lento'
    personagem['cor'] = 'cinza'

for personagem in personagens[:5]:
    print(personagem)

print("Total de personagens=", len(personagens))