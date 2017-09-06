# 165: No seu script coloque sua data de aniversario nos 50 primeiros digitos,
# ex: 080595 faça uma condição se sua data de aniversario estiver nas 50 primeiras linhas print,
# seu aniversario aparece nos primeiros digitos senão,print que ela não aparece.
# use input() para digitar a data explique.

with open("desafio_0164_file") as file:
    arquivo = file.readlines()

pi = ''
for linha in arquivo:
    pi += linha.strip()

birthday = input('Data de aniversario: ')

if birthday in pi[:50]:
    print("Sua data de aniversario aparece nas primeiras 50 casas de pi")
else:
    print("Sua data de aniversario não aparece nas primeiras 50 casas de pi")