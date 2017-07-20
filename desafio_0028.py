# 28: Crie um script que tente acessar uma posição em sua lista, maior que os elementos que nela possui,
# vai ocorrer um erro, explique pq isso acontece.

lista = ["a", "e", "i", "o", "u"]

print(lista[5])

"""
Erro gerado:
IndexError: list index out of range

Esse erro acontece ao tentar acessar um elemento da lista que não existe. Assim é dado um erro de que o
indice que esta tentando acessar esta fora dos limites da lista.
"""