# 6: Crie um script que tenha a idade de uma pessoa em uma variável,
# depois faça a concatenação da idade com duas "strings" adicionando o valor de ambos a outra nova variável,
# ex: nova ="parabéns"+idade+"anos" vai ocorrer um error, então tente resolver e explique pq isso acontece.

idade = 22
nova = "Parabéns, pelos seus " + str(idade) + " anos."

print(nova)

"""
Ao concatenar as duas strings com a idade, que é um inteiro:
nova = "Parabéns, pelos seus " + idade + " anos."

Ocorre o erro:
 TypeError: Can't convert 'int' object to str implicitly
 
Isso acontece porque o Python não consegue reconhecer o tipo de informação da variavel, pois a variavel
tem um valor inteiro armazenado nela, então ela é do tipo int, mas o interpretador do Python não consegue
destinguir se a variavel representa o numero 23 ou os caracteres 2 e 3 juntos. Para usar inteiros nas
strings tem que explicitar isso para o Python, para usar o inteiro como uma string, é possivel fazer isso
usando a função str(variavel), assim o Python converte o intero para a string com os caracteres 2 e 3.
"""