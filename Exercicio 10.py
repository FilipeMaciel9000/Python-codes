#O Dolar ta custando mais ou menos uns 4 reais
#1USS$ = 5.34R$
#1iene=0.50R$
r=float(input('Digite o valor que você tem na carteira: '))
print(r)
d=r/5.34 #Preço atual do dolar
i=r/0.50 #Preço atual do yen
e=r/6.38 #Preço atual do euro
l=r/7.16 #Preço atual da libra
print('Você tem {:.2f}R$\n'.format(r))
print('Com isso você pode comprar: \n{:.2f} Dolares; \n{:.2f} Ienes; \n{:.2f} Euros; \n{:.2f} Libras.'.format(d, i, e, l))
