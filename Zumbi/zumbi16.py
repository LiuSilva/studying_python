# Aula 250 Fatorial de n
n = int(input('Digite n: '))
i = 1
fatorial = 1
while i <= n:
    fatorial *= i
    i += 1
print('Fatorial de %d é %d' % (n, fatorial))
