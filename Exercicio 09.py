'''
Achei melhor fazer logo com a estrutura while
'''
n = int(input ('insera o número da tabuada que você quer estudar: '))
c = 1
i = 1
a = 1
b = 1

print ('Tabuada de adição de {}: \n'.format(n))
while a<= 10:
  som = n+a
  print ('{} + {} = {} \n'.format(n, a, som))
  a+= 1

print('Tabuada de multiplicação de {}: \n'.format(n))
while b<= 10:
  m = n*b
  print ('{} X {} = {} \n'.format(n, b, m))
  b+= 1
  
print ('Tabuada de subitração de {}: \n'.format(n))
while c<= 10:
  sub = (c+n)-n
  print ('{} - {} = {} \n'.format(c+n, n, sub))
  c += 1

print ('Tabuada de divisão de {}: \n'.format(n))
while i<= 10:
  if n == 0:
  print('Não pode dividir por 0 \n ¯\_(ツ)_/¯ \n Lá vai ERROR:')
  else: 
    d = (i*n)/n
    print ('{} / {} = {:.0f} \n'.format(i*n, n, d))
    i += 1
