# 116: No modo interativo crie uma entrada de dados input(), entre com um numero , depois compare esse valor
# ex: idade >= 18 vai ocorrer um error,TypeError: '>=' not supported between instances of 'str' and 'int',
# resolva esse problema e explique.

computer_ask_user = 'Para continuar, digite sua idade: '

user_answer = int(input(computer_ask_user))

if (user_answer >= 18):
    print("Você tem idade suficiente para dirigir!")
else:
    print("Espere ficar mais velho e volte!")

'''
O erro ocorre pois o método input() retorna uma string, assim ao tentar comparar uma string com um inteiro
é gerado o erro. Um modo de resolver isso é por envolver o metodo input() dentro de int(), assim o Python
vai esta sendo avisado explicitamente que ele deve transformar aquele input do usuario, que era uma string,
em um numero inteiro, porque o Python não faz isso implicitamente.
'''