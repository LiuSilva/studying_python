# 169: Crie um script print(5/0) vai acontecer o error ZeroDivisionError,
# use try é except para que mostre uma mensagem "você não pode dividir esses números"..
# ao invez da mensagem de error explique.

try:
    print(5/0)
except ZeroDivisionError:
    print("Você não pode fazer divisões por zero!")