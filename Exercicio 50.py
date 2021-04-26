cont = 0
s = 0
for c in range(1, 7):
    x = int(input('Digite o {} valor: '.format(c)))
    if x % 2 == 0:
        cont += 1
        s += x
print('Do total, a quantidade de números pares ditados foram {} e a soma desses números é {}!'.format(cont, s))