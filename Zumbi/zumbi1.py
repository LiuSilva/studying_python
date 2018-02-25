a = 42
b = 13
print (a + b)

c = 'abacate'
d = ' e banana'
print (c + d)

"""
dir(objeto) é um comando pra saber o que pode fazer com o objeto (funcoes)
help(objeto.funcao) mostra detalhes da funcao
"""

dir (c)
help (c.upper)
help (print)


"""
Dados Logicos
"""

print ("Usando Dados Logicos")

print ('a > b ?')
print (a > b)

print (type (True))

print (type (False))

print ('a == 42 ?')
print (a == 42)

print ('b == 42 ?')

print (b == 42)

print ('a != 13 ?')
print (a != 13)

nota = 7
faltas = 30
print ("notas e faltas usando and")
print (nota >= 6 and faltas <= 20)

print ("Usando or em a e b")
print (a == 42 or b == 42)

print ("\nUsando print")

print ("O número é 33")

a = 42

print ("O número é", a)

print ("O número", a, "é muito legal")

"""
Usando marcador para colocar numeros no meio do print
Marcadores sao de 3 tipos
%d
%f
%s
"""

print ("O número %d é muito legal" %a)

print ("Uma fruta muito gostosa é o %s. Na opnião do Massa" %c)

pi = 3.1415

print ('pi = %f' %pi)

print ('pi = %.2f' %pi)

"""
Python é fortimente tipada e dinamica
"""
a = 'abacate'
a = 42

print (a + 2)

print (str(a) + ' alguma coisa')

a = 42
b = 13

print ("a = ", a)
print ("b = ", b)

a, b = b, a

print ("a = ", a)
print ("b = ", b)

a, b, c = 1, 2, 3

print ("a =", a, ", b =", b, ", c =", c)
