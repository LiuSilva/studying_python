# 144: Faça como o 143, porem com 2 argumentos, tamanho da pizza,
# e o segundo sera as coberturas usando (*) em seguida faça um loop for para mostrar o resultado,
# chame a função e mostre na tela explique.

def coberturas(tamanho, *cobertura):
    print("Tamanho da pizza:", tamanho)
    print(cobertura)

coberturas(12, 'maça', 'presunto', 'mussarela')

coberturas(15, 'mussarela')