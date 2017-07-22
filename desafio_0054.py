# 54: Desafio extra: faça um programa que tenha uma lista de frutas que vc gosta ,
# criei uma copia dessa lista , usando fatiamento, em seguida adicione uma nova fruta a cada lista,
# faça um loop for, mostrando as frutas que vc gosta, e outro para mostrar as frutas que seus amigos gostam.

frutas = ["pera", "goiaba", "maça"]

frutas_segunda_lista = frutas[:]

frutas.append("melancia")

frutas_segunda_lista.append("banana")

print("Minhas frutas:")
for fruta in frutas:
    print(fruta)

print("\nOutras frutas:")
for fruta in frutas_segunda_lista:
    print(fruta)