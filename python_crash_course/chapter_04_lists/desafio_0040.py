# 40: Crie um script com range() quem mostre a saída com números de 1 a 5  em forma de lista explique.

numeros = list(range(1, 6))

print(numeros)

"""
Por o comportamento da funcao range(a, b), gerar numeros de a até b-1, para exibir de 1 a 5, é necessario
passar para o parametro b o numero 5+1, 6, assim ele vai de 1 até 6-1 com a função range. E ao fazer o casting
 do retorno dado pela função range em um tipo list(), a variavel vai receber uma lista de valores de 1 a 5
"""