# 20: Crie um script com uma lista depois armazene um elemento da lista, em uma variável,
# remova o elemento da lista, com o método  .remove() faça a concatenação usando o segundo valor da variável,
# com uma frase ‘string’  observe que o remove apenas elimina a primeira ocorrência explique pq isso acontece .

lista = ["morango", "batata", "maça", "pera", "abacaxi", "manga", "maça", "morango"]

variavel_qualquer = lista[2]

print(lista)

lista.remove(variavel_qualquer)

print(lista)

print("Removeu: " + variavel_qualquer)

"""
O metodo .remove() deleta apenas a primeira ocorrencia do valor especificado, mesmo que a lista repita esse valor
o remove() foi implementado de modo a excluir apenas a primeira ocorrencia, e para que remova todas as ocorrencias
do valor fornecido como parametro é necessario usar um loop pra percorrer toda a lista e remover todas as ocorrencias

"""