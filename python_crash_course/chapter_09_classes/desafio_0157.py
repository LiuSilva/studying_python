# 157: Faça como o 156, Crie outro modulo que contenha a classe Pai e filho <==> import o modulo e a classe filho,
# mostre o resultado da bateria, e das milhas que o carro pode percorrer com a carga total,use (from import)
# obs: são 2 arquivos modulo + desafio explique.

from desafio_0156_carro import CarroEletrico

carro_eletrico = CarroEletrico('Tesla', "A1", 2018)
carro_eletrico.detalhes_carro()
carro_eletrico.bateria.quantia = 85
carro_eletrico.bateria_quatia()

carro_eletrico.bateria.velocidade_atingivel()