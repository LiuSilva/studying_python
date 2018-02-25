# Udemy - 03/01/2017
# Incluindo, Excluindo, Alterando - Aula 59
l = ['bbb', 'ccc', 'ddd']
print(l)

# adicionando no fim da lista
l.append('eee')
print(l)

# escolher posicao para insercao
l.insert(0, 'aaa')
print(l)

l.clear()
print(l)

l = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(l)

# deleta ultimo
print("l.pop() =", l.pop())
print(l)

print("l.pop(0) =", l.pop(0))
print(l)

l = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(l)

# deletar varios
del(l[2:4])
print("del(l[2:4])")
print(l)

l = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(l)

del(l[::2])
print("del(l[::2])")
print(l)