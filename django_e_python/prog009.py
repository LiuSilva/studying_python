#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curso Django e Python - 30/04/2017

@author: luciano

Tipos de Dados Basicos
"""

import sys

print (sys.maxsize)

print()

print("int('123')=", int("123"))

print("int('123', 8)=", int("123", 8))

print()

m = sys.maxsize

print (m)
print (type(m))

m += 1

print (m)
print (type(m))

print()

print("1e+3 =", 1e+3)

print("1e-4 =", 1e-4)

print('-' * 20)

a = "spam"

if a:
    print (a)
else:
    print ("Variavel vazia")
    
b = ""

if b:
    print (b)
else:
    print ("Variavel vazia")
    
    
    