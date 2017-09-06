# 80: Desafio extra: Crie um script com a idade de uma pessoa e de 12 anos,
# nesse caso faça uma condição se idade da pessoa for( < 4: menor que 4 )
# print uma mensagem que ela não pagará, para andar no park,
# se for (< 18:  menor que 18 )ela pagará 5 R$,
# senão: print uma mensagem  que ela pagará 10 R$, use o if-elif -else: explique.

idade = 12

if idade < 4:
    print("Você não paga para andar no park, se divirta!")
elif idade < 18:
    print("Você precisa pagar R$ 5 para andar no park e se divirtir.")
else:
    print("Você precisa pagar R$ 10 para andar no park e se divirtir.")