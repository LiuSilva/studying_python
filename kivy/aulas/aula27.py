# Udemy - 03/01/2017
# Quantidade de Elementos - Aula 61
lista = ['Cláudio', 'José', 'Maria', 'Beltrano', 'Fulano', 'João', 'Ciclano', ]
print(lista)

print("len(lista) =", len(lista))

# Quantidade de elementos repetidos
lista.insert(5, 'José')
print(lista)

lista.append('José')
print(lista)
print("len(lista) =", len(lista))

print("lista.count('José') =", lista.count('José'))

print("lista.count('Maria') =", lista.count('Maria'))

# Onde esta primeira ocorrencia da string informada
print("lista.index('José') =", lista.index('José'))

print("lista.index('Maria') =", lista.index('Maria'))

print(lista)