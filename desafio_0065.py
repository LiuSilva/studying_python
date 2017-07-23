# 65: No modo interativo crie uma string com a 1 letra maiúscula ,
# faça o teste condicional convertendo ela para minúscula , o resultado e True explique.

variavel = "Carro"

print(variavel.lower() == "carro")

'''
Por padrão o Python é case sensitive, assim palavras que sao são iguais, mas tem uma letra maiscula e a outra 
tem minuscula, o teste condicional vai dar False. Mas quando isso não importa, é possivel usar a funcao lower()
para que as comparacoes sejam feitas em palavras minusculas mas sem afetar o valor da variavel original
'''