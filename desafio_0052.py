# 52: Crie um script com uma lista faça a copia dela usando fatiamento, adicione um novo
# elemento diferente  a cada lista 1 e 2, exiba o resultado na tela ,
# cada lista recebe um valor diferente explique.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

lista_copia = lista[:]

lista.append(50)

lista_copia.append(150)

print("Original: ", lista)
print("Copia: ", lista_copia)

"""
Usando o fatiamento a lista1 foi copiada elemento por elemento para lista2, assim no fim tem duas listas
diferentes mas com os mesmos valores, e acrescentar mais valores em uma, nao afeta a outra.
"""