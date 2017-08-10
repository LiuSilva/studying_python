# 122: Crie um script com o loop while, nele vai ter uma variável com valor True,
# se o que o user digitar for diferente de "sair" o loop continua,
# caso contrario, a variável recebe False e o programa terminará, explique.

s = "Digite alguma coisa. Para sair digite 'sair':\n\t"
user = ""
condicao = True

while condicao:
    user = input(s)
    if user != 'sair':
        print('\t->',user)
    else:
        condicao = False