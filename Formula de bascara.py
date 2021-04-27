import math

a = float(input('Qual o valor de a:'))
b = float(input('Qual o valor de b:'))
c = float(input('Qual o valor de C:'))
delta = b**2-4*a*c
if delta == 0:
    x = (-b+math.sqrt(delta))/(2*a)
    print('a raiz desta equação é X=', x)
else:
    if delta < 0:
        print('A equação não possui raizes reais.')
    else:
        x = (-b+math.sqrt(delta))/(2*a)
        y = (-b-math.sqrt(delta))/(2*a)
        print('a raiz desta equação é X={} e y={}:'.format(x, y))
