# 101: Crie um script com um loop for, que mostre apenas os nomes das chaves, no dicionario use keys() explique.

programador = {
    'username' : 'jsnow',
    'nome': "Jon",
    'sobrenome': 'Snow',
    'horas_codificando' : 16,
    'quantia_cafeina' : 300,
    'tempo_sono': 8
}

for chave in programador.keys():
    print(chave)

'''
O metodo .keys() retorna para o for, uma lista com todas as chaves do dicionario
'''