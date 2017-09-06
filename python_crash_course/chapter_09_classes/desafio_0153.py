# 153: Na sua classe crie uma nova instância, e adicione um novo carro,
# crie uma função que incrementa uma nova quilômetragem, ela deverá mudar é receberá um valor de 100,
# mostre o resultado na tela com os 2 valores explique.

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

    def alterar_odometro(self, odometro):
        if odometro >= self.odometro:
            self.odometro = odometro
        else:
            print("Impossível fazer essa atribuição!")

    def add_odometro(self):
        self.odometro += 100

carro = Carro('BMW', 'B2', 2017)
carro.detalhes_carro()
carro.mostrar_odometro()

print("Alterando odometro para 50")

carro.alterar_odometro(50)
carro.mostrar_odometro()

print("Alterando odometro")

carro.add_odometro()
carro.mostrar_odometro()