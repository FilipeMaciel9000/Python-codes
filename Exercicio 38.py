a = int(input('Primeiro numéro: '))
b = int(input('Segundo numéro: '))
if a > b:
    print('O primeiro numéro ({}) é maior que o segundo numéro ({})'.format(a, b))
elif b == a:
    print('Os numéros são iguais')
else:
    print('O segundo numéro ({}) é maior que o primeiro ({})'.format(b, a))