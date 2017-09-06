# 61: Crie uma condição com um loop for, que contenha uma lista de coisas, faça uma condição,
# Se o elemento da lista for igual ao especificado,’string ‘print ele em letras maiúsculas,
# senão : print em minúsculas explique.

lista = ["Celular", "Notebook", "Computador", "Wi-Fi", "desktop", "Linux", "Ubuntu", "Debian", "Kali"]

buscado = "Ubuntu"

for item in lista:
    if item == buscado:
        print(item.upper())
    else:
        print(item.lower())

'''
O comando if serve para comparar se uma certa condição dada é verdadeira ou falsa e com base na avaliação
dessa condição o codigo pode ter comportamentos diferentes.
'''