# Udemy - 02/28/2017
# Break - Aula 50
"""
Debug: coloca breakpoint, roda em debug,
diz a variavel que ele deve mostrar no console do debug
e da F8 pra ir mudando pra instrucao seguinte
"""
print("Antes de entrar no laço")
for item in range(10):
    print(item)
    if item == 6:
        break
print("Depois de ter entrado no laço")