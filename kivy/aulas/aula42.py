# Udemy - 03/02/2017
# Funções Argumentos Posicionais e Nomeados - Aula 77
"""
Argumentos Posicionais: passa valores na ordem que foram implementados
no cabecalho da funcao. Envia como se fosse tupla

Argumentos Nomeados: associa nome do parametro ao valor, faz associacao chave valor.
Envia como se fosse dicionario

"""

def dados_pessoas(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome, sobrenome, idade, sexo))

# Argumento Posicional
dados_pessoas("Claúdio", "Rogério", 30, True)

print()

# Argumento Nomeado
dados_pessoas(sobrenome="Silva",
              nome="Luciano",
              sexo=True,
              idade=22)


