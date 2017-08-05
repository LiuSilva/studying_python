# 107: Crie um script com 3 dicionários cada 1 deles vai ter uma cor e pontuação,
# em seguida faça uma lista e armazene os 3 dicionários,
# crie um loop for que mostre todos os dicionários na lista, essa técnica e chamada de aninhamento explique.

person1 = {'cor': 'verde'}
person2 = {'cor': 'azul'}
person3 = {'cor': 'vermelho'}

lista_person = [person1, person2, person3]

for person in lista_person:
    print(person)

'''
Dentro da lista cada item é um dicionario, e ao iteirar pela lista é retornado um dicionario, seria possível
colocar dentro do for um outro for para recuperar chaves e valores de cada dicionario
Essa tecnica é aninhamento e pode ser bastante util
'''