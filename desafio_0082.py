# 82: Faça a mesma coisa do 81, mais adicione uma condição elif para uma pessoa idosa que vai ser um desconto,
# se idade < 65: preço = 10 mude o preço das outras condições,
# idade < 18: preço = 5
# senão preço = 5 nesse caso qualquer idade abaixo de 65, e de 18 acima,
# a pessoa pagará 10 R$ caso contrario serão executados as outras condições, de acordo com a idade explique.

idade = 12

if idade < 4:
    preco =  0
elif idade < 18:
    preco = 5
elif idade < 65:
    preco = 10
else:
    preco = 5

print("Seu custo de admissão é R$ " + str(preco) + ", para entrar.")

'''
O if é sequencial, se um valor do if é falso, ele checa o primeiro elif, se for falso ele vai para o proximo,
ate chegar no else, caso tudo seja falso. Mas se um deles for True, ele executa o codigo e nao olha os proximos
elif ou else.

Nesse caso se é menor que 4 anos, entra no preco = 0 e imprime a mensagem
Se menor de 18 entra no primeiro elif, preco = 5 e imprime a mensagem
Se maior de 18 e menor de 65 entra no segundo elif, preco = 10 e imprime a mensagem
Se maior ou igual a 65 entra no else, preco = 0 e imprime a mensagem
'''