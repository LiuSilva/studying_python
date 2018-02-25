# coding: utf-8

# Udemy - 03/03/2017
# Funções Variaticas
"""
Funcoes que pode receber quantidade arbitraria de parametros
Elas podem receber 0 ou N parametros, podendo ser posicionais ou nomeados
ou ambos na mesma funcao.

def func(*args, **kwargs): recebe ambos, argumentos posicionais e nomeados

def func(*args): recebe lista de argumentos posicionais

def func(**kwargs): pode receber lista de argumentos nomeados

"""

# recebe lista de argumentos posicionais variaveis
# usa nomeclarura *args no parametro
# recebe tupla
def lista_de_argumentos(*lista):
    print(lista)

# recebe lista de argumentos nomeados variaveis
# usa nomeclarura **kwargs no parametro
# recebe dicionario
def lista_de_argumentos_associativos(**dicionario):
    print(dicionario)

# recebe lista de argumentos posicionais e nomeados variaveis
# posicionais ficam em args, nomeados em kwargs
def argumetos(*args, **kwargs):
    print(args)
    print(kwargs)

print()
argumetos(1, 2, 3, 4, um=1, dois=2, tres=3, quatro=4, cinco=5)

print()
lista_de_argumentos(1, 2, 3, 4, 5, 6)
lista_de_argumentos("um", "dois", "tres", "quatro")

print()
lista_de_argumentos_associativos(a=1, b=2, c=3, d=4)
lista_de_argumentos_associativos(um=1, dois=2, tres=3, quatro=4)