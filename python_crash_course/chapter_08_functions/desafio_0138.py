# 138: Crie um script com uma função que retorne um dicionário, e mostre o resultado explique.

def dados_pessoais(primeiro_nome, ultimo_nome, idade):
    pessoa = {'primeiro_nome': primeiro_nome, 'ultimo_nome': ultimo_nome, 'idade': idade}
    return pessoa

pessoa = dados_pessoais('John', 'Mayer', 27)
print(pessoa)