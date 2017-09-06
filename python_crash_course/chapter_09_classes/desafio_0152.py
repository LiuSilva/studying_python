# 152: Crie uma condição na sua função que atualiza o odômetro, se quilometros for >= quilômetros então,
# odômetro receberá os quilômetros senão, mostrará uma mensagem caso alguém tente reverter o valor explique.

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

carro = Carro('BMW', 'B2', 2017)
carro.detalhes_carro()
carro.mostrar_odometro()

print("Alterando odometro para 50")

carro.alterar_odometro(50)
carro.mostrar_odometro()

print("Alterando odometro para 20")

carro.alterar_odometro(20)
carro.mostrar_odometro()