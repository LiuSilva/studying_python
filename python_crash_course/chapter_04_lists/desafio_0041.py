# 41: Crie um script com um list range() começando de 2 a 10, com intervalo de 2 explique.

numeros = list(range(2, 11, 2))

print(numeros)

"""
A função range() permite acrescentar um terceiro parametro, que por padrao é definido como tendo valor 1,
para ser o tamanho do "salto" entre um numero e outro. Assim fazendo: range(1, 11), como não foi definido
o terceiro parametro que seria o tamanho do "salto", ele vai usar o valor 1, assim gera uma lista pegando
o primeiro numero (parametro fornecido) 1 e acrescenta o valor do "salto", no caso 1, assim vai ser gerado uma
lista de 1 até 10. Mas ao passar o parametro 2 como o tamanho do salto, a função vai mostrar numeros de 2 em 2
assim o primeiro numero fornecido 2, vai ser somado a 2, depois o proximo numero (4) vai ser somado a dois,
e assim sucessivamente ate chegar no numero limite que foi fornecido no segundo parametro.

No exemplo acima a função range comeca de 2 e pula de 2 a 2 até o valor chegar na barreira 11.
"""