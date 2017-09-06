# 96: Desafio extra: crie um script com um personagem,
# no dicionário adicione (posição x, posição y e velocidade)
# exemplo {'posição_x':0 ,'posição_y': 25, 'velocidade': 'medio'} crie condições,
# para a velocidade, se a velocidade  for True,
# então adicione uma variável com um novo valor exemplo incremento = 2
# por ultimo adicione o incremento a posição x e
# print duas mensagens uma no começo mostra a posição original, no final mostra a nova posição explique.

caracter = {
    'name': 'Bob',
    'x': 0,
    'y': 10,
    'speed' : 0
}

print("# Posição Inicial de", caracter['name'], "é x =", caracter['x'], ", y =", caracter['y'])

for i in range(3):

    caracter['speed'] +=  50
    print()
    print("->", caracter['name'], "aumentou a velocidade para", caracter['speed'], "km/s...\n")

    if caracter['speed'] > 0:
        caracter['x'] += caracter['speed']

    print("Posição Atual de", caracter['name'], "é x =", caracter['x'], ", y =", caracter['y'])

print("\n# Posição Final de", caracter['name'], "é x =", caracter['x'], ", y =", caracter['y'])
