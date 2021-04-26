#Crie um programa para calcular o seno, cosseno e tangente
from math import radians, sin, cos, tan
a=float(input('Digite o ângulo que você deseja calcular: '))
seno=sin(radians(a))
print('O ângulo {} tem um seno de {:.2f}'.format(a, seno)) 
cosseno=cos(radians(a))
print('O ângulo {} tem um cosseno de {:.2f}'.format(a, cosseno))
tangente=tan(radians(a))
print('O ângulo {} tem uma tangente de {:.2f}'.format(a,tangente))