# 173: Crie um script com um arquivo de texto, faça uma exceção para caso ele não exista mostrar a msg,
# crie um bloco else para receber o conteudo do arquivo em seguida mostre uma mensagem que imforme
# ex: o arquivo.txt tem 234 palavras. use split() explique

try:
    with open("alice.txt") as file:
        arquivo = file.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
else:
    palavras = arquivo.split()
    numero_palavras = len(palavras)
    print("O arquivo tem", numero_palavras, "palavras.")
