# 150: Faça como o 149,porem adicione um odómetro de 0 km,
# depois mostre o resultado falando que o carro rodou 0 km explique.

class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def detalhes_carro(self):
        print(self.marca, self.modelo, self.ano)

    def mostrar_odometro(self):
        print("O carro tem", self.odometro, "km rodados")

carro = Carro('BMW', 'B2', 2017)
carro.detalhes_carro()
carro.mostrar_odometro()
