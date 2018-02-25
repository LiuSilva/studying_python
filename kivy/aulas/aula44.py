# Udemy - 03/02/2017
# Funções Retorno Multiplo - Aula 78
# retorna tupla
"""
def func():
    return 20, 30

x, y = func()


"""

def func():
    return 1, 2

# quantidade de variaveis deve ser igual a quantidade de valores retornados pela funcao
a, b = func()

print("a=", a)
print("b=", b)

# enpacotamento
tupla = (10, 20)
a, b = tupla

print("a=", a)
print("b=", b)


def potencia(x):
    quadrado = x ** 2
    cubo = x ** 3
    return quadrado, cubo

q, c = potencia(10)

print("q=", q)
print("c=", c)
