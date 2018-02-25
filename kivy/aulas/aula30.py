# Udemy - 03/01/2017
# Operadores AND, OR, IN e NOT IN - Aula 64
"""
verificar se x esta contido em
x and y in [...] lista
x or y in [...] lista

x and y in (...) tupla
x or y in (...) tupla

x and y in {...} dicionario
x or y in {...} dicionario
"""
print("3 in range(1, 6) =", 3 in range(1, 6))

print("3 and 5 in range(1, 6) =", 3 and 5 in range(1, 6))

print("((1 and 6) or (5 and 6) in range(1, 6)) =", ((1 and 6) or (5 and 6)) in range(1, 6))

print("((1 and 3) or (5 and 6) in range(1, 6)) =", ((1 and 3) or (5 and 6)) in range(1, 6))

print()
# Peculiaridade Python
# Quando ele avalia a primeira falsa, ele nao olha as seguintes
print("(10 or 2) in range(1, 6) =", (10 or 2) in range(1, 6))

print("(2 or 10) in range(1, 6) =", (2 or 10) in range(1, 6))

print("10 or 2 in range(1, 6) =", (10 or 2) in range(1, 6))

# Como a primeira retornou falso, o Python nao verifica as seguintes
print("((5 and 6) or (1 and 3) in range(1, 6)) =", ((5 and 6) or (1 and 3)) in range(1, 6))