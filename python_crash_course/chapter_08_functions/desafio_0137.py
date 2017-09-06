# 137: Crie um script com uma função com 3 parâmetros, para o nome completo de uma pessoa,
# o ultimo sera com valor vazio,para caso queira adicionar um segundo nome a pessoa,
# faça uma condição se o parâmetro vazio:então vc criar uma nova variável que receberá,
# os 3 parâmetros senão:, então receberá apenas 2, chame a função das duas formas,
# com apenas 2 nomes, e sem seguida com os 3 explique.

def juntando_nomes(primeiro_nome, ultimo_nome, nome_do_meio=''):
    if (nome_do_meio):
        nome_completo = primeiro_nome + " " + nome_do_meio + " " + ultimo_nome
    else:
        nome_completo = primeiro_nome + " " + ultimo_nome

    return nome_completo

print(juntando_nomes("Luciano", "Silva"))

print(juntando_nomes("Luciano", nome_do_meio='G.', ultimo_nome="Silva"))