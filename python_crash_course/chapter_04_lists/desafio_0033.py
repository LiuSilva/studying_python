# 33: Crie um script com loop for, onde ocorra o error: expected an indented block ,
# esse e um erro de indentação , explique  por que isso acontece.

pessoas = ["João", "Pedro", "Marcos", "Luiza", "Luana", "Ana", "Tiao", "Maria"]

for pessoa in pessoas:
print("Boa tarde " + pessoa + "! Como vc está se sentindo hoje?")

"""
Erro acontece pois Python delimita blocos de codigo usando a identação, se nao identar o código
ele não vai reconhecer quais comandos pertence ao for, e assim ocorre o erro
"""