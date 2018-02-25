# Udemy - 02/28/2017
# Continue - Aula 51
print()
print("Inicio")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    if i > 5:
        break # faz pular o else
    print(i)

else:
    print("else")
print("Fim")
print()