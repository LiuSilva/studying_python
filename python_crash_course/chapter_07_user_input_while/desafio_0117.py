# 117: Crie um script que pergunte a altura de uma pessoa em polegadas para andar no park,
# se a idade >= 36 print altura aprovada,
# senão: print que ela e muito baixa para andar no park e pergunte sua idade, explique.

computer_ask_user = 'Qual sua altura(em polegadas)? '

user_answer = int(input(computer_ask_user))

if (user_answer >= 36):
    print("Excelente! Você pode andar no park!")
else:
    print("Ooh =[ ... Você não tem o requisito minimo de altura para andar no park.\n\tQual sua idade?")
    idade = int(input())
    if idade < 5:
        print('Com', idade + 2, 'anos você vai conseguir andar no park')
    elif idade < 4:
        print('Com', idade + 3, 'anos você vai conseguir andar no park')
    else:
        print('Espere mais alguns anos e você vai poder andar no park.')