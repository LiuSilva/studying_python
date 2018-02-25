# Udemy - 03/01/2017
# Iterando listas em Python - Aula 57
lista_nums = [100, 200, 300, 400]
for item in lista_nums:
    item += 1000
print(lista_nums)

lista_nums = [100, 200, 300, 400]
lista_indice = [0, 1, 2, 3]
for item in lista_indice:
    lista_nums[item] += 1000
print(lista_nums)

lista_nums = [100, 200, 300, 400]
print(lista_nums)
for item in range(4):
    lista_nums[item] += 1000
print(lista_nums)

lista_nums = [100, 200, 300, 400, 500, 600, 700]
print(lista_nums)
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
print(lista_nums)

# usando funcao enumerate, retorna (index, valor)
lista_nums = [100, 200, 300, 400, 500, 600, 700]
print(lista_nums)
for idx, item in enumerate(lista_nums):
    print(item)
    lista_nums[idx] += 1000
print(lista_nums)