n = int(input('Digite o numéro que você deseja estudar: \n '))
x = 1
y = n
z = 1
w = n
print('ADIÇÃO DO NUMÉRO N°{}: '.format(n))
for a in range(1, 11, 1):
    ad = n + x
    print(' {} + {} = {} '.format(n, x, ad))
    x += 1
print('SUBITRAÇÃO DO NUMÉRO N°{}: '.format(n))
for b in range(1, 11, 1):
    s = y - n
    print(' {} - {} = {} '.format(n, y, s))
    y += 1
print('MULTIPLICAÇÃO DO NUMÉRO N°{}: '.format(n))
for c in range(1, 11, 1):
    m = z * n
    print(' {} * {} = {} '.format(n, z, m))
    z += 1
print('MULTIPLICAÇÃO DO NUMÉRO N°{}: '.format(n))
for d in range(1, 11, 1):
    div = w / n
    print(' {} / {} = {:.1f} '.format(w, n, div))
    w += 1