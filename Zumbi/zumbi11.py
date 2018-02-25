# Aula 220 - Imprimir numeros pares de 0 ate numero digitado

n = int(input('Digite um numero: '))
x = 0
while x <= n:
    if x % 2 == 0:
        print(x)
    x += 1
print('Fim')
