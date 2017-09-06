# 163: Edite o arquivo de texto para que ele Mostre as linhas do arquivo em sequencia um a frente do outro,
# é mostre a quantidade de caracters que o arquivo possui explique.

with open('desafio_0161_file') as arquivo:
    arquivo_linhas = arquivo.readlines()

arquivo_completo = ""
for linha in arquivo_linhas:
    arquivo_completo += linha.rstrip()

print(arquivo_completo)
print("Quantidade de caracteres =", len(arquivo_completo))