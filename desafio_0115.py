# 115: Muitas vezes vc pode ter frases longas e não e bom escrever dentro do input(),
# então armazene sua frase em uma variável, em seguida use a variável no input(),
# assim mostrará o resultado que deseja, faça uma concatenação com o resultado digitado pelo usuário,
# com uma frase ficará ex: ola rodrigo !, explique.

computer_ask_user = 'Olá! Para começarmos o seu cadastro no nosso Grupo de Estudos,\nPor favor diga seu nome: '

user_answer = input(computer_ask_user)

print("Olá", user_answer + ", esse foi o primeiro passo para iniciarmos o seu cadastro e te dar acesso ao G.E.P!")
