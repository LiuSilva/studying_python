# 38: Desafio extra: Crie um script que tenha uma lista com pelo menos 3 animais,
# use o loop for com uma declaração para eles , no final do programa faça uma msg declarando o
# que esses animais tem em comum .

animais = ["Cachorro", "Gato", "Leão", "Tigre", "Cavalo", "Onça", "Peixe"]
nomes = ["Bob", "Bixano", "John", "Jack", "Oracio", "Bela", "Peixoto"]

i = 0
for animal in animais:
    print("Ola, eu sou um " + animal + ", meu nome é " + nomes[i] + ", prazer em te conhecer!")
    i += 1

print("")