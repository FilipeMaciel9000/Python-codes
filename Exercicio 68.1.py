"""
@goal: Programa que joga pedra, papel, tesoura com o usuario;
@author: Filipe Rios Maciel Maciel
@date: 05/02/2022
@Declarations:
# Regras do jogo:
1) Os participantes esolhem mentalmente ou pedra ou papel ou tesoura
    E falam pedra, papel, tesoura antes de mostrarem suas escolhas.
2) Depois disso, ambos mostram as mãos:
    a)2 dedos = tesoura;
        *Tesoura corta papel = vitoria de quem escolheu tesoura.
    b)5 dedos = papel;
        *Papel embrulha pedra = vitoria de quem escolheu papel.
    c)mão fechada = pedra
        *Pedra quebra tesoura = vitoria de quem escolheu pedra.
3) Quem ganha: São três rodadas, quem tiver mais vitorias ganha;
(1) Bibliotecas usadas:
(2)
(3)
(4)
(5)
"""
# (1)
from random import choice
from time import sleep

vitoria = 0  # (2)
derrota = 0
empate = 0
jogador = ' '  # (3)
continuar = 'S'
opcoes = ['pedra', 'papel', 'tesoura']  # (4)
print('=' * 50)
while continuar == 'S':
    for v in range(1, 4):  # (5)
        print('Vamos jogar pedra, papel, tesoura!')
        jogador = str(input('Digite pedra, papel ou tesoura para jogar: '))
        computador = choice(opcoes)
        sleep(1)
        print('Pedra')
        sleep(1)
        print('Papel')
        sleep(1)
        print('Tesoura')
        if jogador == "pedra" and computador == 'pedra':
            print('Empate')
            empate += 1
        elif jogador == "pedra" and computador == 'tesoura':
            print('Jogador vence!')
            vitoria += 1
        elif jogador == "pedra" and computador == 'papel':
            print('Computador vence!')
            derrota += 1
        if jogador == "papel" and computador == 'papel':
            print('Empate')
            empate += 1
        elif jogador == "papel" and computador == 'pedra':
            print('Jogador vence!')
            vitoria += 1
        elif jogador == "papel" and computador == 'tesoura':
            print('Computador vence!')
            derrota += 1
        if jogador == "tesoura" and computador == 'tesoura':
            print('Empate')
            empate += 1
        elif jogador == "tesoura" and computador == 'papel':
            print('Jogador vence!')
            vitoria += 1
        elif jogador == "tesoura" and computador == 'pedra':
            print('Computador vence!')
            derrota += 1
        print('Você jogou {} o computador jogou {}!'.format(jogador, computador))
    continuar = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
    print('=' * 50)
    if continuar == 'N':
        break
print('Fim de jogo!')
print('Você ganhou {} vezes; \nEmpatou {} vezes! \nE o computador ganhou {} vezes!'.format(vitoria, empate, derrota))
if vitoria > derrota:
    print('*:･ﾟ✧ ✧ﾟ･: * VITÓRIA DO JOGADOR !!! *:･ﾟ✧ ✧ﾟ･: *')
else:
    print('Vitória do computador!')
print('=' * 50)
