destino = str(input('Para onde você vai viajar: ')).strip().capitalize()
distância = float(input('Digite a distância da viagem em Km: '))
print('Para o destino: {} com a distância de {} Km'.format(destino, distância))
if distância > 200:
    print('O valor da sua passagem será: {:.2f} R$'.format(distância * 0.45))
else:
    print('O valor da sua passagem será: {:.2f} R$'.format(distância * 0.50))