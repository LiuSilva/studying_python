# Udemy - 03/02/2017
# Dicionarios Funções - Aula 73
tel = {
    30301122: "Pericles",
    33547877: "Meenelau",
    33381245: "Atreu",
    36458899: "Tieste"
}

print(tel)

print("len(tel) =", len(tel))

del(tel[36458899])

print(tel)

print()
print("tel.keys() =", tel.keys())

print("tel.values() =", tel.values())

print("tel[30301122]", tel[30301122])

print("tel.get(30301122)", tel.get(30301122))

# popitem tira ultimo e retorna ele em forma d tupla
tel = {
    30301122: "Pericles",
    33547877: "Meenelau",
    33381245: "Atreu",
    36458899: "Tieste"
}

print()
print(tel)
# retorna tupla
print("tel.popitem() =", tel.popitem())
print(tel)
print()

print()
print(tel)
# retorna tupla
print("tel.popitem() =", tel.popitem())
print(tel)
print()

print()
print(tel)
# retorna tupla
print("tel.popitem() =", tel.popitem())
print(tel)
print()

print()
print(tel)
# retorna tupla
print("tel.popitem() =", tel.popitem())
print(tel)
print()

tel = {
    30301122: "Pericles",
    33547877: "Meenelau",
    33381245: "Atreu",
    36458899: "Tieste"
}

print("36458899 in tel =", (36458899 in tel))
print("33333333 in tel =", (33333333 in tel))

tel2 = {999999999: "teste1", 55551111: "teste2"}

print()
print("tel2=", tel2)

# juntando dois dicionarios

tel.update(tel2)

print()
print("tel=", tel)

# relacionar a tupla como chave

tupla = (10, 10, 10)
tel[tupla] = "eXcript"

print()
print("tel=", tel)