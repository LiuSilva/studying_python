# 136: Desafio extra: crie uma função onde terá 2 argumentos , primeiro e ultimo nome,
# em seguida armazene o nome completo a uma variável,
# retorne os valores, com letras maiúsculas, crie um nova variável,
# para armazenar sua função com os nomes, depois print o resultado na tela use (return) explique.

def turning_upper(primeiro_nome, ultimo_nome):
    nome_completo = primeiro_nome + " " + ultimo_nome
    return nome_completo.title()

nome = turning_upper("luciano", "silva")

print(nome)