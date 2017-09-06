# 174: Faça como o 173, mais nesse caso criando uma função def() explique.

def contar_palavras(nome_arquivo):
    """Contando palavras em um arquivo"""
    try:
        with open(nome_arquivo) as file:
            palavras = file.read()
    except FileNotFoundError:
        print("O arquivo", nome_arquivo, "não foi encontrado!")
    else:
        numero_palavras = len(palavras)
        print("O arquivo", nome_arquivo, "tem", numero_palavras, "palavras.")

contar_palavras('alice.txt')
contar_palavras('outro.txt')
contar_palavras('desafio_0160_file')