# 32: Crie um script que mostre uma msg para cada pessoa na sua lista, falando algo para elas,
# em seguida crie outra msg de sua preferência tb fazendo referência as pessoas,
# tudo isso deve funcionar dentro do seu loop for.

pessoas = ["João", "Pedro", "Marcos", "Luiza", "Luana", "Ana", "Tiao", "Maria"]

for pessoa in pessoas:
    print("Boa tarde " + pessoa + "! Como vc está se sentindo hoje?")

print()
print("Vamos começar nossos estudos em Python turma! Todos animados!?")

for pessoa in pessoas:
    print(pessoa + " diz: " + " Siim!!!")