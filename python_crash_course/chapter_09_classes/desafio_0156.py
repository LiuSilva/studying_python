# 156: Crie um modulo para importar sua classe carro depois mostre os resultados na tela obs: são 2 arquivos modulo + desafio explique.

from desafio_0156_carro import Carro, CarroEletrico

carro = Carro('BMW', 'B2', 2017)
carro.detalhes_carro()

print()

carro_eletrico = CarroEletrico('Tesla', "A1", 2018)
carro_eletrico.detalhes_carro()
carro_eletrico.bateria_quatia()

carro_eletrico.bateria.velocidade_atingivel()