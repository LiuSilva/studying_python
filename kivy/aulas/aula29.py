# Udemy - 03/01/2017
# Operadores IN e NOT IN - Aula 63
"""
verificar se x esta contido em
x in [...] lista
x in (...) tupla
x in {...} dicionario
"""

print("2 in (1, 2, 3, 4, 5)", 2 in (1, 2, 3, 4, 5))
print("6 in (1, 2, 3, 4, 5) =", 6 in (1, 2, 3, 4, 5))
print("6 not in (1, 2, 3, 4, 5) =", 6 not in (1, 2, 3, 4, 5))
print("1 in range(1, 6) =", 1 in range(1, 6)) # 1 esta entre 1 a 5?
print("6 in range(1, 6) =", 6 in range(1, 6))
print("list(range(1, 6)) =", list(range(1, 6)))

x = range(1, 6)
print("x=", list(x))
if 3 in x:
    print("3 - Contido")
else:
    print("3 - Não contido")

if 1 in x:
    print("1 - Contido")
else:
    print("1 - Não contido")

if 0 in x:
    print("0 - Contido")
else:
    print("0 - Não contido")