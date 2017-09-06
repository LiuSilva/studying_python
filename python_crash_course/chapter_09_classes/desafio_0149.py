# 149: Crie uma classe para um carro, que mostre marca modelo e ano explique.

class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes_carro(self):
        print(self.marca, self.modelo, self.ano)

carro = Carro('BMW', 'B2', 2017)
carro.detalhes_carro()