# Udemy - 03/01/2017
# Tuplas - Aula 62
"""
Tupla tem mesma funcoes das listas, mas é somente para leitura
mas as Tuplas são estuturas de dados heterogenias

Tudo que estiver entre parenteces é definicao de tupla
tudo que estiver entre cochetes é lista

objetos separados por virgulas tambem sao tuplas

Tupla é somente para leitura, nao da pra alterar nem excluir
"""

# Definindo tupla
t = tuple("abc")
print(t)

print("type( (1, 2, 3) ) =", type( (1, 2, 3) ))

x = "aaa", 1, True
print("x =", x)
print("type(x) =", type(x))