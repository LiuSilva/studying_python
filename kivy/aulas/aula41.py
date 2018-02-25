# Udemy - 03/02/2017
# Funções Parametros Default - Aula 76
# precisam ser os ultimos do cabecalho
# os parametros sem argumento default vem primeiro
# por ultimo os que tem parametros default

def login(usuario="root", senha="123"):
    print("Usuário:", usuario)
    print("Senha:", senha)

login()

print()
login("Claúdio")

print()
login("root", "1234")

"""
Se fosse assim, teria que definir o valor do sistema, pois ele nao tem valor default
e se nao informar da erro

def login(sistema, usuario="root", senha="123"):
    print("Usuário:", usuario)
    print("Senha:", senha)

"""