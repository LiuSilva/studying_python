# 161: Faça como o 160, porem use a função rstrip() pra remover as linhas em branco explique.

with open('desafio_0161_file') as arquivo:
    arquivo_completo = arquivo.read()
    print(arquivo_completo)
    print()
    print(arquivo_completo.rstrip())