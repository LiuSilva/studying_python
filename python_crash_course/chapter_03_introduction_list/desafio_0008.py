# 8: Crie um script que mostre apenas o primeiro elemento da lista passando a posição e explique como funciona.

lista = [1, 5, 10, 15, 20, 25]

print(lista[0])

"""
As listas são uma coleção de dados, e os elementos são "ordenados" de 0 ao numero total de elementos na lista
para acessar qualquer elemento dentro da lista, basta usar [] e o valor do indice do elemento, lembrando
que em Python o primeiro elemento tem o indice igual a zero.
Desse modo toda lista em Python começa de 0 até N-1, com N sendo o valor total de itens na lista.

Uma lista com 10 elementos, os indices para acessar esses elementos vão de 0 até 9,
sendo 0 o indice do primeiro elemento, e 9 o indice do decimo elemento da lista com 10 itens. 
"""