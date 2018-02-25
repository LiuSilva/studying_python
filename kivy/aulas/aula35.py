# Udemy - 03/02/2017
# Propriedades String - Aula 69
s = "Lista de Caracteres"
print("len(s) =", len(s))
print("len('') =", len(''))
print("len('0') =", len('0'))
print(s)
print("s[6] =", s[6])
print("s.split(' ') =", s.split(' '))

print("Usando split")
lista = s.split(" ")
print(lista)
print(lista[0] + " " + lista[2])

print('s.replace("de ", "") =', s.replace("de ", ""))
