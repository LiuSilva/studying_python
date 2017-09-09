from book011_001_name_function import get_nome_completo

print("Digite 'q' para sair")
while True:
    first_name = input('Digite o primeiro nome: ')
    if first_name == 'q':
        break

    last_name = input('Digite o ultimo nome: ')
    if last_name == 'q':
        break

    nome_completo = get_nome_completo(first_name, last_name)
    print("O nome completo: ", nome_completo)

