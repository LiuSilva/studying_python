# 16: Crie um script que remova o ultimo elemento da lista de forma que vc ainda possa usar o elemento removido.
# explique  o método.

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

print(lista)

ultimoItem = lista.pop()

print(lista)

print("Ultimo elemento = " + str(ultimoItem))

"""
O metodo pop() remove o ultiimo elemento de uma lista, mas ele retorna esse item, para ser possível usá-lo
assim, no exemplo acima, ao usar o .pop(), o valor do ultimo elemento da lista é copiado para variavel
ultimoItem, e depois removido da lista. Assim é possivel usar o ultimo elemento mesmo ele tendo sido removido
da lista.
"""