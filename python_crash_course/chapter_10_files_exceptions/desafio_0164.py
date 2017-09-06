# 164: Faça com que seu script mostre as primeiras 50 casas decimais, para casos de muitas linhas explique.

with open("desafio_0164_file") as file:
    arquivo = file.readlines()

pi = ''
for linha in arquivo:
    pi += linha.strip()

print(pi[:52])
print("Quantidade de caracteres =", len(pi))