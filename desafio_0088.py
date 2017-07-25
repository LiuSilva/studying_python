# 88: Desafio extra: crie uma lista vazia, em seguida faça uma condição( if) rápida para a lista,
# python retorna True se a lista tiver pelo menos um elemento,
# nesse caso não tem, então o resultado e False,
# crie um loop for com uma mensagem concatenando com os elementos da lista,
# já que não tem nada para a pizza,
# então faça uma mensagem perguntando se a ‘pessoa deseja uma pizza simples’ use o else:.

ingredientes = []

if ingredientes:
    for item in ingredientes:
        print(item, "adicionado")
    print("Pizzar pronta!")
else:
        print("Você realmente deseja uma pizza simples?")