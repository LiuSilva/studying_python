import json

file_name = 'username.json'

try:
    with open(file_name) as file:
        username = json.load(file)
except FileNotFoundError:
    username = input("Qual seu nome? ")
    with open(file_name, 'w') as file:
        json.dump(username, file)
        print("Eu vou me lembrar do seu nome", username + ", quando você voltar!")
else:
    print("Bem vindo novamente", username + "!")