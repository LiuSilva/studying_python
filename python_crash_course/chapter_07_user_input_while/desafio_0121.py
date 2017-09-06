# 121: Crie um script com o loop while, que enquanto a mensagem digitada pelo usuário
# for != diferente de sair, ele executara o loop explique.

s = "Digite alguma coisa. Para sair digite 'sair':\n\t"
user = ""

while user != 'sair':
    user = input(s)
    print('\t->',user)

'''
Enquanto condição do while for true (texto diferente de sair), ele vai repetir o laço
'''