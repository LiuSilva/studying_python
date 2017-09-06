# 31: Crie um script que mostre uma mensagem “string”, para cada elemento da sua lista,
# usando o loop for, explique.

carros = ["A4", "Bravo", "C4", "Celta", "Civic", "Ducato", "EcoSport", "Fusion", "Hilux", "SW4"]

print("Os carros disponíveis são:")
for carro in carros:
    print(carro + " é um carro muito confortável e barato! É uma otima escolha para sua familia.")

print("Qual você deseja comprar?")

"""
O for vai colocar cada elemento da lista na variavel carro, seguindo a ordem da lista carros
assim o for vai iterar por toda a lista e em cada iteração um dos elementos vai ser armazenado na variavel
carro, e assim o codigo identado depois do for, vai ser repetido ate chegar no ultimo elemento da lista
isso faz com que o print() seja executado em cada iteração e desse modo mostrar todos os itens contidos na lista.
"""