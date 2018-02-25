# aula 240 Media de 10 numeros
n = 1
soma = 0
while n <= 10:
    x = int (input('Digite o %d número: ' % n))
    soma += x
    n += 1
print("Soma: %d" % soma)
print("Média: %.2f" % (soma/10))
