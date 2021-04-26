#Faça um sorteio
import random
n1=input('Canditado: ')
n2=input('Canditado: ')
n3=input('Canditado: ')
n4=input('Canditado: ')
n5=input('Canditado: ')
lista=[n1, n2, n3, n4, n5]
x=random.choice(lista)
print('O sorteado foi ===> {} !'.format(x))