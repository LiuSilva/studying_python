# 89: Crie um script com duas listas de coberturas para pizza, coberturas disponíveis,
# e uma com pedidos das pessoas,
# faça um loop se a cobertura estiver nas coberturas disponíveis,
# vai ser exibida a mensagem ex ‘adicionando tomate’ ...
# senão vai mostrar uma mensagem ex: ‘não temos batata frita no momento’.

coberturas_disponiveis = ["Pimenta", "Uvas", "Batata frita", "Bacon", "Catupiri"]

pedidos = ["Batata frita", "Chocolate", "Açaí",]

for pedido in pedidos:
    if pedido in coberturas_disponiveis:
        print(pedido.title(), "adicionado")
    else:
        print("Não temos", pedido, "no momento!")

print("Pizza pronta!")