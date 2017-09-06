# 125: Crie um script com loop infinito explique.

numero = 0

while numero < 10:
    # numero += 1 # ao esquecer o incremento que faz o while parar, ele entra em loop infinito
    if numero % 2 == 0:
        continue
    print(numero)


'''
sempre que a condição do while não consegue atingir valor false ou o loop nao é abortado usando break
tem um loop infinito
'''