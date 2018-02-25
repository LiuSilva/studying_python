# aula 250 Break
soma = 0
while True:
    x = int(input('Digite o número (0 sai): '))
    if x == 0:
        break
    soma += x
print ('Soma: %d' % soma)
