# 170: Desafio extra: Crie uma pequena calculadora, para a divivisão de 2 números usando o loop while,
# se você dividir 5/0 por exemplo, vai ocorrer o error que você viu antes,
# faça com que seja exibida uma mensagem para quando ocorrer esse error
# ex: "você não pode dividir o 0 " se a divisão ocorrer corretamente então mostrarar o resultado da divisão, explique.

prompt = 'Dividindo dois números\n' \
         'Digite "q" para sair'

while True:
    num1 = input('Primeiro número: ')
    if num1 == 'q':
        break

    num2 = input('Segundo número: ')
    if num2 == 'q':
        break

    try:
        resultado = int(num1) / int(num2)
    except ZeroDivisionError:
        print("Impossível divisão por zero!")
    else:
        print(resultado)