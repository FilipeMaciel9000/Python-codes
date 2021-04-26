from math import hypot
co=float(input('Digite o valor do catetos opostos: '))
ca=float(input('Digite o valor dos catetos adjacentes: '))
hi=hypot(co, ca)
print('A hipotenusa vale {:.2f}'.format(hi))