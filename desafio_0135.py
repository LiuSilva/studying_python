# 135: Crie uma função com argumentos,parâmetro e adicione valores a eles,
# em seguida chame a função sem fazer suas declarações, vai ocorrer um erro explique.

def funcao_qualquer(numero, expoente):
    print(numero, "elevado a", expoente, " é igual a", numero ** expoente)

funcao_qualquer(2, 10)

funcao_qualquer()

'''
Python reconhece que tem informações faltando na chamada da funcao, e como valores padroes nao foram definidos
ocorre o erro
'''