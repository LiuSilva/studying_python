# 42: Crie um script com duas variáveis , a 1 com uma lista vazia ficará (fora) do loop,
# a 2 vai receber um range de números de 1 a 10 (dentro) do loop for ao quadrado **,
# por último adicione os valores da segunda  variável a lista vazia, explique o método.

numeros = []

for i in range(1, 11):
    numero = i ** 2
    numeros.append(numero)

print(numeros)

"""
Dentro do for vai ser colocado na variavel "numero" o quadrado no numero "i" em cada iteracao do for
e esse valor vai ser armazenado na lista "numeros", assim sucessivamente ate o fim do loop for
"""