# 57: Crie um script com uma tupla e alguns elementos, tente substituir  um elemento dela ,
# vai acontecer um error explique .

tupla = (5, 50)

tupla[1] = 100

print(tupla[-2])
print(tupla[-1])

'''
O erro que acontece é 
TypeError: 'tuple' object does not support item assignment

Esse erro acontece ao tentar modificar algum elemento da tupla, por ela ser definida como uma lista imutável,
tentar alterar algum de seus valores gera o erro acima.
'''