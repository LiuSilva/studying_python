#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curso Django e Python - 29/04/2017

@author: luciano

Atribuição
"""

a = 0
print ("a = ", a)
a += 1
a += 1
print ("a += 2 => ", a)

print ()

print ("a = ", a)
a *= 3
print ("a *= 3 => ", a)

print ()

a = 'a'
print ("a = ", a)
a *= 3
print ("a *= 3 => ", a)

print ()

a = 1
b = 2

print ("a =", a, "b =", b)

b, a = a, b

print ("a =", a, "b =", b)