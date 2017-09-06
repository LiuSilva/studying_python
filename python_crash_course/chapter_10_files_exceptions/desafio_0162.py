# 162: Faça com que seu arquivo de texto possa manter o acesso fora do bloco, é mostre o resultado use readlines() explique.

with open('desafio_0161_file') as arquivo:
    arquivo_linhas = arquivo.readlines()

for linha in arquivo_linhas:
    print(linha)

print()
for linha in arquivo_linhas:
    print(linha.rstrip())