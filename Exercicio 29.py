print('---####---' * 5)
x = float(input('Digite a velocidade do veiculo em Km/h: '))
print('---####---' * 5)
if x >= 81:
    print('\33[0;31;40m---####---\33[0;31;40m'* 5)
    print(' Você Ultrapassou o limite de velocidade;\n Precisa pagar uma multa no valor de {:.2f}R$;\n Dirija com '
          'cuidado!'.format((x - 80) * 7))
    print('---####---' * 5)
else:
    print('---####---' * 5)
    print(' Você está dentro do limite de velocidade;\n Não precisa pagar nenhuma multa.\n Dirija com cuidado!')
    print('---####---' * 5)
