# 59: Crie um script com uma tupla e 2 elementos ,faça um loop for na primeira e print o resultado ,
# em seguida altere o valor da variável  com a tupla,
# novamente  repita outro loop abaixo com a variável alterada,  e mostre o resultado explique.

print("Tupla")
tupla = (2, 3, 4, 5, 6, 1, 7, 8, 9, 0)
for i in tupla:
    print(i)

print("\n Nova Tupla")

tupla = (i for i in range(0, 20, 2))
for i in tupla:
    print(i)

'''
Em tuplas não é possivel modificar, adicionar novos elementos, mas é possivel atribuir a variavel uma nova tupla
assim a antiga é apagada e a variavel passa a armazenar a nova tupla
'''