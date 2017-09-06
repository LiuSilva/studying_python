# 99: Crie um script com um dicionário que tenha o username de uma pessoa,
# o primeiro nome, e o ultimo a cada par de chaves,
# em seguida faça um loop for para mostrar as chaves e os seus valores, use .items() explique

programador = {
    'username' : 'jsnow',
    'nome': "Jon",
    'sobrenome': 'Snow',
    'horas_codificando' : 16,
    'quantia_cafeina' : 300,
    'tempo_sono': 8
}

for chave, valor in programador.items():
    print(chave, "=", valor)

'''
O metodo items(), retorna a chave e valor de cada atributo contido no dicionario, de forma a ser possível 
iterar por todos os dados contidos no dicionario
'''