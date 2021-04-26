maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Voluntario {}; por favor insira seu peso kg: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if maior > peso:
            maior = peso
        if menor < peso:
            menor = peso
print('Maior peso lido {}Kg'.format(maior))
print('Menor peso lido {}Kg'.format(menor))
