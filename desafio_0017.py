# 17: Crie um script que  remova o ultimo elemento da lista com método pop(), armazene em uma segunda variável,
# e faça a concatenação dele com uma frase “string” que comece com a primeira letra maiúscula .

lista = ["item1", "item2", "item3", "item4", "item5", "item6"]

ultimoElemento = lista.pop()

print("Acessando o ultimo elemento depois de remove-lo, o " + ultimoElemento.title() + ", era o ultimo da lista.")