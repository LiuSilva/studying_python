# Udemy - 02/28/2017
# Operadores Relacionais - Aula 34
numero1 = input('Digite um número: ')
numero1 = int(numero1)

numero2 = input('Digite um outro número: ')
numero2 = int(numero2)

if numero1 == numero2:
    print("O número %d é igual a %d. "%(numero1, numero2))
if numero1 != numero2:
    print("O número %d é diferente de %d. "%(numero1, numero2))
if numero1 < numero2:
    print("O número %d é menor que %d. "%(numero1, numero2))
if numero1 > numero2:
    print("O número %d é maior que %d. "%(numero1, numero2))
if numero1 >= numero2:
    print("O número %d é maior ou igual que %d. "%(numero1, numero2))
if numero1 <= numero2:
    print("O número %d é menor ou igual que %d. " % (numero1, numero2))