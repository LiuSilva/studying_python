# 43: Faça a mesma coisa do (42) só que sem a variável dentro do loop explique.

numeros = []

for i in range(1, 11):
    numeros.append(i ** 2)

print(numeros)

"""
O codigo vai fazer exatamente o mesmo que o desafio 42, porem nao vai usar a variavel temporaria "numero"
dentro do for, o resultado da operaçao i ** 2, i elevado a 2, vai ser acrescentado na lista sem a necessidade
de uma variavel extra pra salvar o resultado da operacao
"""