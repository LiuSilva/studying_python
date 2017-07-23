# 72: Repita os desafios do 70 e 71, porem usando (OR ) explique .

idade1 = 17

idade2 = 10

if idade1 < 18 or idade2 < 18:
    print("Um de vocês é menor de idade!")
else:
    print("Vocẽs são adultos! Sejam responsáveis!")

print()

idade1 = 18

idade2 = 20

if idade1 < 18 or idade2 < 18:
    print("Um de vocês é menor de idade!")
else:
    print("Vocẽs são adultos! Sejam responsáveis!")

'''
O operado OR faz com que duas condições sejam verdadeiras se alguma das duas forem verdadeiras, esse é o OU lógico
apenas False e False gera um False, o restante faz o resultado do OR ser True
'''