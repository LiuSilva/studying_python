# aula 140 latas de tinta
# uma lata pinta 54 metros

metros = int(input('Quantidade de metros quadrados: '))
if metros % 54 != 0:
    latas = int(metros / 54) + 1
else:
    latas = metros / 54

valor = latas * 80

print ('%d lata(s) a custo de %.2f' %(latas, valor))
