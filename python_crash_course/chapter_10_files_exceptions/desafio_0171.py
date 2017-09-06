# 171: Crie um script que tente ler um arquivo que não exista,
# exemplo rodrigo.txt vai ocorrer o error FileNotFoundError:
# use try except para mostrar uma mensagem falando que o arquivo.txt não existe explique.

file_name = 'rodrigo.txt'

try:
    with open(file_name) as file:
        content_file = file.read()
except FileNotFoundError:
    print("Arquivo '" + file_name + "' não encontrado!")