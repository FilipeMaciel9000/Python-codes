#Aluguel automobilistico dias e km rodados
print('Quanto será que vou paga no aluguel do carro???')
print('Sendo que o aluguel custa 60R$ por dia mais 0,15 centavos por Km rodado.')
x=int(input('Por quantos dias você ficou com o carro?'))
y=float(input('Quantos quilometros você rodou com ele?'))
z=(x*60)+(y*0.15)
print('Bom.\n Se você alugou esse carro por{} dias.\n E rodou por {:.2f} Km.\n O aluguel que você vai paga é de {} R$\n.'.format(x,y,z))
