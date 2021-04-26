# O jogo da adivinhação
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
print('-=-=-' * 15)
print('{} ### A D I V I N H A ### {}'.format(cores['amarelo'], cores['limpa']))
print('{}Vou pensar em um numéro entre 0 e 5; você vai tentar advinhar!{}'.format(cores['verde'], cores['limpa']))
print('{}Se você acertar o numéro que eu pensar você ganha!{}'.format(cores['verde'], cores['limpa']))
print('-=-=-' * 15)
esc = int(input('{}Escolha o seu numéro entre 0 e 5: {}'.format(cores['verde'], cores['limpa'])))
computador = randint(0, 5)
print('{}Processando resultado . . .{}'.format(cores['verde'], cores['limpa']))
sleep(2)
if esc != computador:
    print('-=-=-' * 15)
    print('{}Eu ganhei{}'.format(cores['vermelho'], cores['limpa']))
    print('Eu pensei em ->{}<- não no seu número ->{}<-'.format(computador, esc))
    print('-=-=-' * 15)
    print('Aperte o play para tentar de novo')
else:
    print('-=-=-' * 15)
    print(' {}*:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧{} {}PARABÊNS{} {}*:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧{}'.format(cores['azul'], cores['limpa'], cores['amarelo'],cores['limpa'],cores['azul'],cores['limpa']))
    print(' {}*:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧{} {}Você adivinhou o numéro que pensei!{} {}*:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧ {}'.format(cores['azul'], cores['limpa'], cores['verde'],cores['limpa'],cores['azul'],cores['limpa']))
    print(' {}*:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧{} {}PARABÊNS{} {}*:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧{}'.format(cores['azul'], cores['limpa'], cores['amarelo'],cores['limpa'],cores['azul'],cores['limpa']))
    print('-=-=-' * 15)
    print('Aperte o play para jogar de novo')
