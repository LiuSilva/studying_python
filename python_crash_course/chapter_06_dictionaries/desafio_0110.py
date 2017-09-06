# 110: Crie um script com um dicionário, com coberturas pra uma pizza,
# 1 chave vai ter o tipo da pizza, a 2 vai ser uma lista dentro do dicionário,
# faça um loop e resuma o pedido da pessoa, informando qual o tipo da pizza,
# e as coberturas que estão na lista explique.

pizza = {
    'tipo': 'Portuguesa',
    'coberturas': ['queijo', 'azeitona', 'mussarela', 'linguiça', 'catupiri']
}

print("Sua pizza", pizza['tipo'], 'possui a seguinte cobertura:')
for cobertura in pizza['coberturas']:
    print('\t' + cobertura.title())

print("\nBom apetite!")