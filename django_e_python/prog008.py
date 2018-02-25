#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Curso Django e Python - 29/04/2017

@author: luciano

Comandos exec
"""

exec ("a = 1")

print (a)

ls = exec ("import os; os.system('ls -l')")
print (ls)