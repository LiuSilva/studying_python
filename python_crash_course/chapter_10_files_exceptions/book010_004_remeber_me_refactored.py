import json

def get_stored_username():
    """Lendo nome armazenado"""
    file_name = 'username.json'
    try:
        with open(file_name) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Pedir o usuario o nome"""
    username = input("Qual seu nome? ")
    file_name = 'username.json'
    with open(file_name, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    """Cumprimentando um usuario pelo seu nome"""
    username = get_stored_username()
    if username:
        print("Bem vindo novamente", username + "!")
    else:
        username = get_new_username()
        print("Eu vou me lembrar do seu nome", username + ", quando você voltar!")

greet_user()
