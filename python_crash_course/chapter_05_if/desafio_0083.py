# 83: Faça o mesmo do 82, porem mude a condição else: para se a idade do idoso for >= 65 preço = 5,
# o resultado será basicamente a mesma coisa.

idade = 12

if idade < 4:
    preco =  0
elif idade < 18:
    preco = 5
elif idade < 65:
    preco = 10
elif idade >= 65:
    preco = 5

print("Seu custo de admissão é R$ " + str(preco) + ", para entrar.")