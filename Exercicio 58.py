from random import randint

computador = randint(1, 10)
print('>>> Computador: \n Estou pensando em um número ente 1 e 10 \n Qual é o número?')
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Insira seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais... Tente de novo!')
        if jogador > computador:
            print('Um pouco menos... Tente de novo: ')
print('Acertou miseravi!')
print('Acertou com {} tentativas!'.format(palpites))
