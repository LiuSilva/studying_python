# 100: Faça como  o 98, porem com um loop for,
# mostrando as chaves com o nome de cada pessoa e sua linguagem favorita exemplo
# ‘rodrigo sua linguagem favorita e : Python ...’ use items() explique.

linguagens_programacao = {
    'Pessoa1' : 'JavaScript',
    'Pessoa2': 'PHP',
    'Pessoa3': 'HTML/CSS',
    'Pessoa4': 'Java',
    'Pessoa5': 'Python'
}

for chave, valor in linguagens_programacao.items():
    print(chave, "você gosta de programar na linguagem", valor)

'''
O metodo items(), retorna a chave e valor de cada atributo contido no dicionario, de forma a ser possível 
iterar por todos os dados contidos no dicionario
'''