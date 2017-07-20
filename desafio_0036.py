# 36: Crie um script que tenha uma lista, faça 3 msgs, as 2 primeiras vão ter interação com a lista no loop for,
# a 2 msg , vai ter uma quebra de linha no final \n , a 3 msg  vai ser uma qualquer dentro do loop,
# vai acontecer uma desordem nas msgs, tente arrumar e explique, oque aconteceu.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you everyone, that was a great magic show!")

"""
Colocar a terceira mensagem ainda com a identacao do for, o Python vai entender que o codigo ainda
pertence ao for, mesmo tendo uma quebra de linha entre o ultimo print e os dois primeiros

Para corrigir isso deveria tirar a identacao da ultima mensagem, assim ela seria executada apenas
uma vez, pois não faz parte do comando for.
"""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone, that was a great magic show!")