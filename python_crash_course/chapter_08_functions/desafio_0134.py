# 134: Faça como o 131, porem adicione um valor padrão ao tipo de animal no parâmetro,
# depois chame a função e mostre na tela o resultado explique.

def animal_mensagem(nome_animal, tipo_animal="Dragon"):
    print("O animal escolhido é um", tipo_animal)
    print("O nome do", tipo_animal, "é", nome_animal)
    print()

animal_mensagem(tipo_animal="Giant Wolf", nome_animal='Ghost')

animal_mensagem('Drogon')

'''
Ao definir um valor padrão, caso aquele campo não for fornecido, ele vai usar o valor definido como sendo o padrao
mas se passar os dois parametros, o valor padrao é sobrescrito.
'''