# Udemy - 03/02/2017
# Exemplo Prático de IN - Aula 65
a = 10
b = 25
c = 66

x = int(input('Digite um número: '))
if x in [a, b, c]:
    print("Está contido.")
else:
    print("Não está contido.")

cores = ["azul", "amarelo", "vermelho", "branco"]

while True:
    cor = input("Difite o nome de uma cor ou então, "
                "0 para sair do programa: ")
    if cor == "0":
        break
    elif cor in cores:
        print("Essa cor está contida.")
    else:
        print("Essa cor Não está contido.")
    print()