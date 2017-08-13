# 140: Crie um script com uma função, primeiro e segundo nome nos args(),
# faça uma variável que receba o nome completo, depois retorne o valor, faça um loop while,
# crie duas variáveis para o usuário digitar primeiro e segundo nome,
# faça com que ele posso sair,digitando 'q',
# em seguida crie uma variável pra armazenar sua função passe os valores, depois chame a função explique.

def formando_nome(primeiro_nome, ultimo_nome):
    nome_completo = primeiro_nome + " " + ultimo_nome
    return nome_completo.title()

while True:
    print("Informe seu nome e sobrenome, para sair digite 'q'")
    primeiro_nome = input('Digite seu primeiro nome: ')
    if primeiro_nome == 'q':
        break

    ultimo_nome = input('Digite seu sobrenome: ')

    pessoa_nome = formando_nome(primeiro_nome, ultimo_nome)
    print("\n\tSeja bem vindo", pessoa_nome, "\n")