from random import randint
from time import sleep
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30;40m',
         'pretoecinza': '\033[7:30m',
         'matrix': '\33[0;32;40m',
         'rubronegro': '\33[0;31;40m', }
print(''' 
##### JOKENPO #####
Vamos jogar pedra papel tesoura:
Suas opções de escolha:
[0]Pedra
[1]Papel
[2]Tesoura
''')
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
escolha = int(input('Escolha uma das três opções acima para jogar: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-> Computador jogou {}'.format(itens[computador]))
print('-> Jogador jogou {}'.format(itens[escolha]))
if computador == 0: #computador escolheu pedra
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('{}VÍTORIA DO JOGADOR{}'.format(cores['azul'], cores['limpa']))
    elif escolha == 2:
        print('{}VÍTORIA DO COMPUTADOR{}'.format(cores['rubronegro'], cores['limpa']))
    else:
        print('{}JOGADA INVALIDA{}'.format(cores['vermelho'], cores['limpa']))
elif computador == 1: #computador escolheu papel
    if escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('{}VÍTORIA DO JOGADOR{}'.format(cores['azul'], cores['limpa']))
    elif escolha == 0:
        print('{}VÍTORIA DO COMPUTADOR{}'.format(cores['rubronegro'], cores['limpa']))
    else:
        print('{}JOGADA INVALIDA{}'.format(cores['vermelho'], cores['limpa']))
elif computador == 2: #computador escolheu tesoura
    if escolha == 2:
        print('EMPATE')
    elif escolha == 1:
        print('{}VÍTORIA DO COMPUTADOR{}'.format(cores['rubronegro'], cores['limpa']))
    elif escolha == 0:
        print('{}VÍTORIA DO JOGADOR{}'.format(cores['azul'], cores['limpa']))
    else:
        print('{}JOGADA INVALIDA{}'.format(cores['vermelho'], cores['limpa']))