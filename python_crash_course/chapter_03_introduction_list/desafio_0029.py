# 29: Desafio extra: Crie um programa que tenha: (uma lista de carros, um comprador, e um vendedor)
# o vendedor vai falar: seja bem vindo. O comprador vai perguntar quantos carros tem na concessionária,
# use o len() para isso, em seguida, o comprador faz outra pergunta. Quais são os carros?
# O vendedor vai Responder: quais são ,  passe a posição de cada carro, que seja exibida todos com letras maiúsculas.
# O comprador vai gostar de um carro , então faça uma frase, que fale qual carro , ele gostou passando a posição.
# Por último ele pergunta o preço , o vendedor responde: , e ele dar risada e fala que está barato

carros = ["A4", "Bravo", "C4", "Celta", "Civic", "Ducato", "EcoSport", "Fusion", "Hilux", "SW4"]

vendedor = "João"

comprador = "Marcos"

print(vendedor + " diz: Seja bem vindo, " + comprador + "!")
print()

print(comprador + " diz: Quantos carros tem na concessionária?")
print()

print(vendedor + " diz: Hoje temos " + str(len(carros)) + " carros. Você gostaria de ve-los " + comprador + "?")
print()

print(comprador + " diz: Sim, me mostre quais são.\n")

print(vendedor + " diz: Os carros são: " + carros[0].lower() + ", " + carros[1].lower() + ", " + carros[2].lower() + ", "
      + carros[3].lower() + ", " + carros[4].lower() + ", " + carros[5].lower() + ", " + carros[6].lower() + ", "
      + carros[7].lower() + ", " + carros[8].lower() + ", " + carros[9].lower() + "." )
print()

print(comprador + " diz: Eu gostei do " + carros[4] + ", qual é o preço dele?")
print()

print(vendedor + " diz: R$ 60 000,00!\n")

print(comprador + " diz: hahaha Está muito barato! Vou levar!")

