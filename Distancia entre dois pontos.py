import math

xa=int(input('Digite o valor correspndente a coordenada:'))
xb=int(input('Digite o valor correspndente a coordenada de um outro ponto no mesmo plano:'))
ya=int(input('Digite o valor correspndente a coordenada:'))
yb=int(input('Digite o valor correspndente a coordenada de um outro ponto no mesmo plano:'))
d=math.sqrt((xb-xa)**2+(yb-ya)**2)
if d>=10:
    print('longe')
else:
    print('perto')
