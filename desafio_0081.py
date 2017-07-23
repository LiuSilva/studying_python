# 81: Crie um script onde a idade da pessoa e de 12 anos, se a idade,
# for < 4: o preço = 0 se for < 18: preço = 5
# senão: preço = 10 ,
# por ultimo faça uma mensagem ‘Seu custo de admissão e $' concatenando com o preço,
# converta o preço para str()  use if-elif-else: explique.

idade = 12

if idade < 4:
    preco =  0
elif idade < 18:
    preco = 4
else:
    preco = 10

print("Seu custo de admissão é R$ " + str(preco) + ", para entrar.")

'''
O codigo faz o print uma vez so, e usa a variavel no if-elif-else para saber o valor que deve ser
exibido para o usuario, isso fica mais claro o codigo.
'''