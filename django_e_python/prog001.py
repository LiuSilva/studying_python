#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Curso Django e Python - 29/04/2017

@author: luciano

Exemplo de Programa
"""

import random

numero = random.randint(1,100)

tentativas = 0

escolha = 0

while escolha != numero:
    escolha = int(input("Informe um número entre 1 e 100: "))
    tentativas += 1
    if escolha > numero:
        print ("Maior")
    elif escolha < numero:
        print("Menor")

print ("Acertou! O número sorteado era", numero)
print ("Você usou", tentativas, "tentativas")
