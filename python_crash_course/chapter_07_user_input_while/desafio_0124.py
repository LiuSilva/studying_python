# 124: Crie um script com o loop while, onde tenha uma variável com um contador 0,
# enquanto contador for < 10 contador recebe += 1, se o contador % 2 == 0 for igual a 0,
# então ele terá que ignorar esses resultados, se == 1,
# ele retorna os números que tiveram o %1 use (continue), explique.

numero = 0

while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue
    print(numero)