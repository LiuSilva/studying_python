# Udemy - 03/02/2017
# Dicionarios - Aula 71, 72
# Lista que é associado é a uma chave
# temos que gerenciar os indices e valores do dicionario
# qualquer objeto pode ser uma chave.
# tuplas podem ser chaves tambem
# listas nao podem ser chaves
# Tudo que esta entre chaves é reconhecido como dicionario

d1 = {}
d2 = dict()

print("d1 = {}, type(d1) =", type(d1))
print("d2 = dict(), type(d2) =", type(d2))

d1['aaa'] = 1000
print(d1)

d1['bbb'] = 2000
d1['ccc'] = 3000
print(d1)

print("d1['bbb'] =", d1['bbb'])

print()
d2 = {1.1: "teste1", 2.2: "teste2", 3: "teste3"}
print(d2)
print(d2[1.1])
print(d2[3])