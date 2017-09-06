# 127: Muitas vezes vc pode ter em uma lista mais de um elemento, por exemplo uma lista de animais,
# que tenha gato mais de uma vez, use o loop while,
# pra remover esses animais da sua lista com o método remove() explique.

lista = ['Cachorro', 'Gato', 'Macaco', "Gato", "Pato", "Gato", "Gato"]

print(lista)

while "Gato" in lista:
    lista.remove("Gato")

print(lista)