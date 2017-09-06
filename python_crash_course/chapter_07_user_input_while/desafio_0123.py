# 123: Crie um script com o loop while onde o usuário vai digitar os lugares que ele visitou,
# se o que ele digitar for igual a "sair" o loop acaba, e o programa termina,
# senão será concatenado uma mensagem com a o valor digitado pelo
# usuário, ex:" Eu adoraria ir para SP" use 'break' explique.

s = "Diga um lugar que você ja visitou. Para sair digite 'sair':\n\t"
user = ""

while True:
    user = input(s)
    if user != 'sair':
        print('\tEu adoraria ir para', user)
    else:
        break