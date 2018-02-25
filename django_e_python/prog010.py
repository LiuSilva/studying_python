#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curso Django e Python - 30/04/2017

@author: luciano

Tipos de Dados Sequencias
Strings: Imutavel
Listas: Mutavel
Tuplas: Imutavel
"""

a = "spam"
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print()
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])

print("\n\n Slice")

a = "spam eggs ham"
print (a)

# O primeiro indice é incluido, o ultom nao
print ("a[5:9] =", a[5:9])

print ("a[5:9] + a[9:] =", a[5:9] + a[9:])

print("a[::2] =", a[::2])

# fazer copia simples
print("a[:] =", a[:])


print("\n\n Iterar na lista")

a = [1, 2, 3, 4, 5]

print (a)

for i in a:
    print (i)
    
print("\n\n Fazer uma lista de outra")

a = list(range(10))
print ("a =", a)

b = []

for i in a:
    b.append(i ** 2)
    
print ("b =", b)

# usando uma outro modo do Python

print ("a =", a)

c = [i ** 2 for i in a]

print ("c =", c)


print ("a =", a)

d = [i ** 2 for i in a if i % 2]
print ("d =", d)


# string 

regex = r"(\w)"
print ("Regex =", regex)

# strings são imutaveis

"""
Concatenar strings é algo custoso pois ele cria nova string e desaloca a anterior
para mihares de iterações isso fica pesado

Melhor fazer uma lista de strings depois um join

append é mais eficiente

join é mais rapido
"""

a = []

for i in range(100):
    a.append(str(i))

print (a)

print(''.join(a))


print()

pi = 3.1415

print("%s: %.2f" % ("pi", pi))

print ()

d = {'nome': "Fulano", 'email' : "fulano@cicrano.com"}

print ("Nome: %(nome)s - E-mail: %(email)s" % d)

print ()

a = "spam eggs ham"
print ('a =', a)

print ("a.split() =", a.split())

print ("a.split('eggs') =", a.split('eggs'))

print()

a = "spam eggs ham\nfoo\nbar\nbaz"
print ('a =', a)

print ("a.split() =", a.split())

b = a.split()

print ('b =', b)

print ('"\\n".join(b) =', '\n'.join(b))

print ('"::".join(b) =', '::'.join(b))

print("\n\nStrip")

a = "   \n\n\t\tXYZspamZYX     "

print ("a =", a)

print("\na.strip() = ", a.strip())

print("\na.lstrip() = ", a.lstrip())

print("\na.rstrip() = ", a.rstrip())

print("\na.strip(' ') = ", a.strip(' '))

print("\na.strip(' \\n') = ", a.strip(' \n'))

print("\na.strip('\\n \\tXY') = ", a.strip('\n \tXY'))

a = "spam eggs ham"

print ("\na.startswith('spam') =", a.startswith('spam'))

print ("\na.startswith('eggs') =", a.startswith('eggs'))

print ("\na.endswith('ham') =", a.endswith('ham'))

print ("\n'x' in 'spam' =", 'x' in 'spam')

print ("\n'x' not in 'spam' =", 'x' not in 'spam')

print ("\na.find('eggs')", a.find('eggs'))

print ("\na.index('eggs')", a.index('eggs'))

print ("\na.find('foo')", a.find('foo'))

#print ("\na.index('foo')", a.index('foo')) # da excecao

# fazem a mesma coisa mas é melhor usar index

print ("\na.upper() =", a.upper())
