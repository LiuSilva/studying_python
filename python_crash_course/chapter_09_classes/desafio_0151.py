# 151: Crie uma função na sua classe para atualizar o odômetro, depois adicione o valor dele para 23 km,
# mostre na tela no resultado explique.

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
        self.odometro = odometro

carro = Carro('BMW', 'B2', 2017)
carro.detalhes_carro()
carro.mostrar_odometro()

print("Alterando odometro para 50")

carro.alterar_odometro(50)
carro.mostrar_odometro()