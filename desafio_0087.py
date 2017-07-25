# 87: Faça como 86, porem faça uma mensagem se  ‘elemento’ == a um elemento na lista,
# print ex: ‘desculpe estamos sem pimenta’, depois dessa mensagem use o else: para o resto do código.

ingredientes = ["Tomate", "Queijo", "Presunto", "Bacon", "Azeitona", "Pimenta"]

for item in ingredientes:
    if item == "Pimenta":
        print("Desculpe, estamos sem Pimenta.")
    else:
        print("Adicionando", item, ".")

print("Pizza Pronta!")