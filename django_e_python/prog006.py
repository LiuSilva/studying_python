#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curso Django e Python - 29/04/2017

@author: luciano

Comandos for
"""

a = [("key1", "value1"), ("key2", "value2"), ("key3", "value3"), ("key4", "value4")]

for chave, valor in a:
    print ("Chave =", chave, "- Valor = ", valor)
    
for i in range(10):
    print (i)
    
print ();

a = ["spam", "eggs", "foo", "bar", "qoox"]

for i, elemento in enumerate(a):
    print (i, elemento)