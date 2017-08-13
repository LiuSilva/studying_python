# 141: Crie um script com uma função,e um loop for,
# crie uma variável para armazenar uma mensagem com os valores que serão repetidos print a msg,
# em seguida faça uma lista com os nomes dos usuários que sua função vai receber,
# chame a função passando a lista com os nomes explique.

def boas_vindas_ao_grupo(nomes):
    for nome in nomes:
        boas_vindas = "Olá " + nome.title() + ", seja bem vindo ao grupo de estudos de Python!\n"
        print(boas_vindas)

pessoas = ['Rodrigo', 'Luiza', 'Greicy', 'Patricia', 'Michael', 'Luciano']
boas_vindas_ao_grupo(pessoas)