# 139: Crie um script com uma função que tenha um dicionário,que vai receber 3 argumentos
# primeiro nome, segundo e idade, idade sera vazio,
# faça uma condição se idade: então adicione chave e argumento ao dicionário,
# retorne o dicionário,crie uma variável que recebe a função adicione o primeiro e segundo nome
# e por ultimo a idade, explique.

def dados_pessoais(primeiro_nome, ultimo_nome, idade=0):
    if idade:
        pessoa = {'primeiro_nome': primeiro_nome, 'ultimo_nome': ultimo_nome, 'idade': idade}
    else:
        pessoa = {'primeiro_nome': primeiro_nome, 'ultimo_nome': ultimo_nome}
    return pessoa

pessoa1 = dados_pessoais('John', 'Mayer', 27)
pessoa2 = dados_pessoais('Ed', 'Sheeran')

print(pessoa1)
print(pessoa2)