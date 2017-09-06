# 154: Crie uma nossa classe para a bateria do seu carro,
# onde a classe filho deverá herda uma mensagem que mostre a bateria do carro
# ex:"O carro tem 70-kWh de bateria." por fim mostre o resultado na tela explique.

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

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, bateria=70):
        super().__init__(marca, modelo, ano)
        self.bateria = bateria

    def bateria_quatia(self):
        print("O carro tem", self.bateria, "-kWh de bateria")


carro = Carro('BMW', 'B2', 2017)
carro.detalhes_carro()

carro_eletrico = CarroEletrico('Tesla', "A1", 2018)
carro_eletrico.detalhes_carro()
carro_eletrico.bateria_quatia()