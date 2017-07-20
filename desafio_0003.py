# 3: Crie um script que contenha uma frase em uma variável sobre aspas simples,
# e faça ocorrer o error de invalid syntax:
# faça a mesma coisa com aspas duplas, e depois explique por que o error acontece.

frase = 'I'm a "Python" student'

print (frase)

frase = "I'm a "Python" student"

print (frase)

'''
Ao delimitar um string com aspas simples, e colocar um apostrofe na frase, vai gerar o erro de
invalid syntax, e também ao colocar alguma palavra da frase entre aspas duplas 
dentro da string delimitado com aspas duplas.

O erro acontece porque o interpretador do Python não reconheceu alguma coisa no código como sendo um 
código válido do Python, ao delimitar um string com aspas simples, tudo que estiver entre a primeira
aspa simples e a segunda é considerado a string, se tiver mais texto depois de fechar as aspas simples,
o Python considera que aquilo seria algum código Python e dá o erro invalid syntax.

Para colocar " " dentro da string, ela tem que ser delimitada com aspas simples, e para usar apostrofe ou
aspas simples no texto a string tem que ser delimitada com aspas duplas. 

Uma outra alternativa para colocar aspas dentro do texto é usar o operador \ antes das aspas, como se segue:
frase = "I\'m a \"Python\" student"

Deste modo ia ser possível usar tanto aspas simples, como duplas dentro da string sem que o Python gerasse o
erro de sintaxe invalida.

'''