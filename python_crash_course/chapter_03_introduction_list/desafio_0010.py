# 10: Mostre o ultimo elemento da lista, passando a posição de forma negativa e explique .

lista = ["primeiro elemento", "segundo elemento", "terceiro elemento", "quarto elemento", "quinto elemento"]

print(lista[-1])

print(lista[-5])

"""
O Python tem um recurso diferente de outras linguagens de programação, que ele permite indices negativos,
o que geraria um erro em varias linguagens usar um indice de lista negativo. Mas o Python usa os indices negativos
para acessar a string de trás pra frente. Assim ao usar o indice -1, é retornado o ultimo elemento da lista
se usar -2, retorna o penultimo item da lista, e assim sucessivamente ate -n

No caso do exemplo acima, sao 5 elementos, então:
0, 1, 2, 3, 4, acessa os elementos da lista na ordem de inserção, do primeiro, segundo.
-1, -2, -3, -4, -5, acessa os elementos da lista começando do ultimo elemento (-1), ate o primeiro elemento(-5)
"""