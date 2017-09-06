# 34: Crie um script com uma lista , exiba 2 msgs na tela, ambas vão ter interação com o loop for,
# a segunda msg  estará fora do bloco, e so vai ser executada ao final do loop,
# apenas o ultimo elemento da lista aparecerá na 2msg, explique por que isso acontece.

pessoas = ["João", "Pedro", "Marcos", "Luiza", "Luana", "Ana", "Tiao", "Maria"]

for pessoa in pessoas:
    print("Boa tarde " + pessoa + "!")

print("Vamos começar!?")

"""
A indentação faz com que a frase de boa tarde esteja dentro do bloco do for e vai ser executada em cada
iteração do for.
Ja a frase vamos la tem identação diferente e esta fora do bloco for.. assim ela so executa uma vez no final.
"""
