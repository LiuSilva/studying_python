# Udemy - 03/01/2017
# Listas - Aula 54
lista = [1, 2, 5, 8, 10, 15, 3, 6, 8]

print(lista)
print("type(lista) =", type(lista))
print("type([]) =", type([]))
print("type(['asv', 2, 'dfe']) =", type(['asv', 2, 'dfe']))
print("lista[0] =", lista[0])
print("lista[3] =", lista[3])
print("lista[5] =", lista[5])

# Passando lista para criar um objeto list
lista1 = list("eXcript")
print(lista1)

lista = list((4, 5, 6))
print(lista)

lista = list(("eXcript"))
print(lista)

print("Usando , no fim da lista")
lista = list(("eXcript",))
print(lista)

# no Python é comum colocar , no fim da lista para ele distinguir o que deve ser lista

print(['aaaf', 'adasdsa', 3, 8, ])

a = (5)
print("a = (5) type(a) =", type(a))

a = (5, )
print("a = (5, ) type(a) =", type(a))