# 128: Crie um script com loop while, que faça duas perguntas ao usuário, qual seu nome,
# e qual montanha ele gostaria de escalar, em seguida, adicione as respostas a um dicionário,
# faça outra pergunta caso outra pessoa queira responder,
# ela deve digitar (sim /não) se ele digitar não, o loop deve acabar,
# terá que mostrar na tela ex: --resultado da enquete-- rodrigo gostaria de escalar no Alasca, explique.

respostas = {}

while True:
    nome = input("Qual é o seu nome? ")
    montanha = input("Qual montanha você gostaria de escalar algum dia? ")

    respostas[nome] = montanha

    parada = input("Você se importaria de deixare outra pessoa responder? (sim / não) ")

    if parada.lower() == 'não'.lower():
        break

print("---- Resultado da Pesquisa ----")

for nome, montanha in respostas.items():
    print(nome.title(), "gostaria de escalar o", montanha)