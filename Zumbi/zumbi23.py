# Aula 273
vetor = []
i = 1

while i <= 10:
    n = int(input('Digite um número: '))
    vetor.append(n)
    i += 1

print('Vetor lido:', vetor)

i = 9
vetor_inverso = []
while i >= 0:
    vetor_inverso.append(vetor[i])
    i -= 1

print('Vetor invertido:', vetor_inverso)
