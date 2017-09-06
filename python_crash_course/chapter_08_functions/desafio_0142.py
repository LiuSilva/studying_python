# 142: Crie um script com uma função com 2 argumentos, faça um laço while
# onde uma variável vai receber cada ultimo item de sua lista durante o loop,
# e vai jogar para uma lista secundaria, crie outra função que mostre todos os itens da nova lista
# usando o loop for, por ultimo chame as duas funções e mostre na tela o resultado explique.

def processando_listas(lista1, lista2):
    while lista1:
        lista2.append(lista1.pop())

def mostrar_lista(lista):
    print(lista)

lista1 = ["A", "B", "C", "D", "E"]
lista2 = []

processando_listas(lista1, lista2)
mostrar_lista(lista1)
mostrar_lista(lista2)