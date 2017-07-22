# 9: Crie um loop for com a função range() com números de 1 a 5, a saída são apenas números de 1 a 4,
# explique por que isso acontece.

for i in range(1,5):
    print(i)

"""
Isso acontece porque a função range(a, b), mostra os numeros de "a" ate "b-1", a função para quando atinge o
segundo numero fornecido como parametro e não inclui esse numero na lista criada, é como se ele fosse a
barreira para a função, então ela pode ir ate antes da barreira (que é o numero b)
"""