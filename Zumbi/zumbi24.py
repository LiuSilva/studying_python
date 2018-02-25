# Aula 274
notas = []
i = 1
soma = 0
while i <= 4:
    n = int(input('Nota: '))
    notas.append(n)
    soma += n
    i += 1
print('Notas:', notas)
print('Média: %4.2f' % (soma/4))
