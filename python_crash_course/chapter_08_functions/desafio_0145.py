# 145: Crie um script com 3 argumentos primeiro nome e segundo, o 3 vai ser as informações do user,
# crie um dicionário vazio, em seguida adicione primeiro e segundo nome ao dicionário,
# faça um loop for use items(),onde o dicionário vai receber ['chave']= valor retorne o dicionário,
# chame a função e adicione primeiro e segundo nome,em seguida local e trabalho.
# obs: o ultimo argumento vc usará args(**) explique.

def info_user(first_name, last_name, **add_info):
    person = {}
    person['first_name'] = first_name
    person['last_name'] = last_name
    for key, value in add_info.items():
        person[key] = value
    
    return person

person = info_user('Luciano', 'Silva', local='MG', trabalho='Developer')
print(person)