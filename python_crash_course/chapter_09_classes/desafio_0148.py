# 148: Crie com uma classe com parâmetros para um cachorro,nome idade,
# faça 3 funções que vão receber essas definições,1 fala que ele esta sentado,
# 2 fala que ele esta por toda parte, 3 fala que ele esta rolando, depois crie duas instancias,
# cada instancia sera um cachorro diferente, em seguida use as funções para cada cachorro e mostre na tela explique.

class Cachorro():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(self.nome, "está latindo!")

    def rolar(self):
        print(self.nome, "está rolando!")

    pass

cachorro_um = Cachorro('Jon', 2)
cachorro_dois = Cachorro('Dany', 3)

cachorro_dois.latir()
cachorro_um.rolar()