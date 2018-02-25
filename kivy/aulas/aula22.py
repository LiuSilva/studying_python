# Udemy - 03/01/2017
# Listas - Aula 56

# concatenacao de duas listas com sinal de adição
lista = [1, 2, 3, 4, 5]
print(lista)

lista = lista + [6]
print("lista = lista + [6] =", lista)

lista = [0] + lista
print("lista = [0] + lista =", lista)

lista += [7, 8, 9, 10]
print("lista += [7, 8, 9, 10] =", lista)

print()
# adicionando elemento na lista
lista.append(11)
print("lista.append(11) =", lista)

lista.append([11])
print("lista.append([11]) =", lista)

# excluir elemento da lista
del(lista[-1])
print("lista.append(11) =", lista)

# adicionar elementos iguais
print("10 * [0] =", 10 * [0])

lista += 10 * [0]
print("lista += 10 * [0] =", lista)

print("50 * '-' =", 50 * '-')