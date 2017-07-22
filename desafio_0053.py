# 53: faça a mesma coisa do 52, sem usar o fatiamento, ambas as listas vão receber os 2 valores,
#  explique pq isso acontece.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

lista_copia = lista

lista.append(50)

lista_copia.append(150)

print("Original: ", lista)
print("Copia: ", lista_copia)

"""
Sem usar o fatiamento a lista2 vira uma referencia da lista1, assim no fim tem uma unica lista
com duas referencias para ela, e acrescentar mais valores em uma, afeta a outra.
"""