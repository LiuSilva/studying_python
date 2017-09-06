# 76: Crie um script que tenha uma lista com users banidos,
# caso o usuário não esteja na lista vai exibir uma mensagem ‘você já pode enviar sua resposta agora’
# use o (in )e (not) para isso, explique.

banned_users = ["Marcos", "João", "Lucas", "Mateus", "Zack"]

user = "Pedro"

if user not in banned_users:
    print(user + ", você já pode enviar sua resposta agora!")
else:
    print(user + ", você está banido do grupo!!!")

'''
O not faz o resultado gerado pelo in ser invertido, assim se um nome não estiver na lista o resultado será
True ao invés de False, e se o valor procurado estiver na lista, sera retornado True.
'''