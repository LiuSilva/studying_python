# Udemy - 03/02/2017
# Iterando String - Aula 70

# Exemplo 1
s = "Iterando Strings"

for c in s:
    print(c)

print()

# Exemplo 2
indice = 0

while indice < len(s):
    print(indice, s[indice])
    indice += 1

print()

# Exemplo 3
for key, value in enumerate(s):
    print(key, value)