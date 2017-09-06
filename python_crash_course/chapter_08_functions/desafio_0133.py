# 133: Muitas vezes vc pode trocar a ordem dos argumentos,parâmetros em uma função,
# e ter um resultado fora de ordem em seu programa, existe uma forma de concertar isso,
# argumentos de palavras chaves, faça na sua função e mostre o resultado na tela explique.

def dados_pessoais(nome, idade, cidade):
    print("Nome  :", nome)
    print("Idade :", idade)
    print("Cidade:", cidade)
    print()

dados_pessoais(cidade='Winterfell', nome='Jon Snow', idade=26)
dados_pessoais(nome='Daenerys', idade=25, cidade='DragonStone')

'''
Ao usar as palavras chaves a ordem dos parametros não importa, mas sem usar a passagem de parametros usando as 
palavras chaves, a ordem de definição da função deve ser seguida para que os valores sejam designados as variaveis
corretas.
'''