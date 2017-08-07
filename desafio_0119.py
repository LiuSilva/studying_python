# 119: Desafio extra: crie um script que pergunte um valor que ao dividir,
# fale se o valor e par ou impar use (%) explique.

numero = int(input('Digite um número inteiro qualquer: '))

if numero % 2 == 0:
    print("O número", numero, 'é um numéro par!')
else:
    print("O número", numero, 'é um numéro impar!')