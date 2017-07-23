# 85: Faça como o 84 porem adicione elifs depois do if ,
# o código vai parar na primeira condição caso ela passe, explique por que isso acontece.

ingredientes = ["Tomate", "Queijo", "Presunto", "Bacon", "Azeitona"]

if "Queijo" in ingredientes:
    print("Queijo adicionado!")
elif "Tomate" in ingredientes:
    print("Tomate adicionado!")
elif "Presunto" in ingredientes:
    print("Presunto adicionado!")
elif "Bacon" in ingredientes:
    print("Bacon adicionado!")
elif "Azeitona" in ingredientes:
    print("Azeitona adicionado!")

'''
O if com elif, só executa executa uma das opções, se uma delas é verdadeira, ele não executa as outras,
assim se tivesse varios ifs, todos seriam verificados, mas ao usar a estrutura if-elif-else, apenas um
dos codigos vai ser executado, o que fazer a condição verdadeira.
'''