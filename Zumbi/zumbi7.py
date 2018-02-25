"""
aula 130
Faça um programa que leia três números e mostre o maior deles.

"""

a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))

if a >= b and a >= c:
    print ('Primeiro: %d' %a)
elif b >= c:
    print ('Segundo: %d' %b)
else:
    print ('Terceiro: %d' %c)
