#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curso Django e Python - 29/04/2017

@author: luciano

Comandos while
"""
a = 0
while a < 10:
    print (a)
    a += 1
else:
    print("Fim")

print()
a = 0
while a < 10:
    print (a)
    a += 1
    if a > 5:
        print ("Interrompido")
        break
else:
    print("Fim")
