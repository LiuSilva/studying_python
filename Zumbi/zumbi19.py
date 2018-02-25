# Aula 265
'''
Sequencia de Fibonacci
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3

YouTube -> Nature by Numbers
'''

n = int(input('N: '))
a, b = 1, 1
k = 1

while k <= n - 2:
    a, b = b, a + b
    k += 1

print('Fib(%d) = %d' %(n, b))
