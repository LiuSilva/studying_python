# 45: Crie um script com o mesmo resultado dos desafios anteriores 42,43 com apenas 1 linha dento de uma lista []
# essa forma e chamada de Lista de Compreensões explique.

numeros = [i ** 2 for i in range(1, 11)]

print(numeros)

'''
O Python diferente de outras linguagens tem o recurso de listas de compreensao que é possivel criar listas
em apenas uma linha de codigo, usando o comando for dentro dos parentesses da criacao da linha
Assim cada resultado da iteracao do for vai ser adicionado na lista
'''