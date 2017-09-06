# 126: Desafio extra: crie um script com um loop while, fora dele vai ter duas listas,
# 1 com users não confirmados, e outra com usuários confirmados,
# dentro do while vc terá uma variável que recebe cada ultimo user da lista durante o loop while,
# que fara com que cada usuário passe por uma verificação,
# e depois disso sera movido para a lista de confirmados em seguida faça um loop for,
# que mostre cada usuário confirmado explique.

users_confirmados = []

users_nao_confirmados = ['Joao', 'Jose', 'Maria', 'Pedro', 'Mateus', 'Marcos', 'Lucas', 'Timoteo']

while users_nao_confirmados:
    user = users_nao_confirmados.pop()

    print("Verificando o usuario", user, "...")

    users_confirmados.append(user)

print("Usuarios confirmados:\n")
for user in users_confirmados:
    print("\t", user)

