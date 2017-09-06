# 155: Crie uma função com uma condição na classe bateria(),se o tamanho da bateria== 70: variável = 240 para caso contrario
# faça um elif que receberar == 270, faça uma variável que receberá uma mensagem, para ser exibida de acordo com a condição,
# ex:"Esse carro pode ir aproximadamente 240 milhas com uma carga total", depois mostre o resultado na tela explique.

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

class Bateria():
    def __init__(self, quantia):
        self.quantia = quantia

    def velocidade_atingivel(self):
        if self.quantia == 70:
            velocidade = 240
        elif self.quantia == 85:
            velocidade = 270

        print("Velocidade atingivel é", velocidade)



class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, bateria=70):
        super().__init__(marca, modelo, ano)
        self.bateria = Bateria(bateria)

    def bateria_quatia(self):
        print("O carro tem", self.bateria.quantia, "-kWh de bateria")


carro = Carro('BMW', 'B2', 2017)
carro.detalhes_carro()

carro_eletrico = CarroEletrico('Tesla', "A1", 2018)
carro_eletrico.detalhes_carro()
carro_eletrico.bateria_quatia()

carro_eletrico.bateria.velocidade_atingivel()