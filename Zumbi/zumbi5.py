# condições em Python - aula 110

a = int (input ('Primeiro valor: '))
b = int (input ('Segundo valor: '))

if a > b:
    print ('O primeiro número é o maior!')
if b > a:
    print ('O segundo número é o maior!')

idade = int(input ('Digite a idade de seu carro: '))

if idade <= 3:
    print ("Seu carro é novo")
if idade > 3:
    print ("Seu carro é velho")

idade = int(input ('Digite a idade de seu carro: '))

if idade <= 3:
    print ("Seu carro é novo")
else:
    print ("Seu carro é velho")


velocidade = int (input ('Qual a velocidade: '))

if velocidade > 110:
    print ("Você foi multado!")
    valor = (velocidade - 110) * 5
    print ("Valor da multa R$", valor, "reais!")
