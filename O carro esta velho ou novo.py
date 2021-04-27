tempo_carro=int(input('Quantos anos o seu carro tem?'))
print('{}; né...'.format(tempo_carro))
if tempo_carro <= 2:
    print('O carro está novinho')
elif tempo_carro <= 5:
    print('O carro esta meio que seminovo')
else:
    print('O carro já tá velho!')