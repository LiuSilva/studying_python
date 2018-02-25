#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curso Django e Python - 29/04/2017

@author: luciano

Comandos if/elif/else
"""

a = int(input("A: "))
b = int(input("B: "))

if a > b:
    print ("A é maior que B")
elif a < b:
    print ("B é maior que A")
else:
    print ("A e B são iguais")

print ("A é maior" if a > b \
       else "A não é maior")

c = "A é maior que 0" if a > 0 else "A é menor que 0"

print (c)