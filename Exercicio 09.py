'''
Achei melhor fazer logo com a estrutura while
'''
n = int(input(' Digite o numero da tabuada que você quer estudar: \n '))
x = 1
y = 1
z = 1
w = 1
print('DIVISÃO°{}\n'.format(n))
while x <= 10:
    d = x / n
    print('{} / {} = {:.2f}'.format(x, n, d))
    x += 1
print('Multiplicação°{}\n'.format(n))
while y <= 10:
    m = n * y
    print('{} * {} = {}'.format(n, y, m))
    y += 1
print('SUBTRAÇÃO°{}\n'.format(n))
while z <= 10:
    s = z - n
    print('{} - {} = {}'.format(z, n, s))
    z += 1
print('ADIÇÃO°{}\n'.format(n))
while w <= 10:
    a = n + w
    print('{} + {} = {}'.format(n, w, a))
    w += 1
