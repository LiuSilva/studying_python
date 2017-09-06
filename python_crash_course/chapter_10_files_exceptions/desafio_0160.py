# 160: Armazene seu arquivo de texto em uma variável, depois mostre o seu conteudo com um loop for explique.

with open('desafio_0160_file') as arquivo:
    arquivo_linhas = arquivo.readlines()

for linha in arquivo_linhas:
    print(linha.strip())