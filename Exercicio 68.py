"""
@goal: Programa que joga par ou impar com o usuario;
@author: Filipe Rios Maciel Maciel
@date: 25/01/2022
@Declarations: Regras do jogo:
1) Os participantes apostam em par e ímpar.
2) Depois disso, ambos mostram as mãos escondendo alguns dedos.
3) Contam-se os dedos e vence quem tiver acertado a paridade do número de dedos.
"""
from random import randint
vitoria = 0
tipo = " "
print('='*45)
while tipo not in 'PI':
    while True:
        tipo = str(input('Par ou ímpar (P ou I): ')).strip().upper()[0]
        jogador = int(input('Escolha um número de 0 a 5: '))
        computador = randint(0, 5)
        soma = jogador + computador
        print('Você jogou {}. \nO computador jogou {}. \nO resulado é {}!'.format(jogador, computador, soma))
        if tipo == 'P':
            if soma % 2 == 0:
                print('*:･ﾟ✧ ✧ﾟ･: *')
                print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧PARABÉNS✧ﾟ･: *ヽ(◕ヮ◕ヽ)')
                print('*:･ﾟ✧ ✧ﾟ･: * VITÓRIA DO JOGADOR !!! *:･ﾟ✧ ✧ﾟ･: *')
                print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧PARABÉNS✧ﾟ･: *ヽ(◕ヮ◕ヽ)')
                print('*:･ﾟ✧ ✧ﾟ･: *')
                vitoria += 1
            else:
                print('VITÓRIA DO COMPUTADOR !!!')
                break

        elif tipo == 'I':
            if soma % 2 == 1:
                print('*:･ﾟ✧ ✧ﾟ･: *'*3)
                print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧PARABÉNS✧ﾟ･: *ヽ(◕ヮ◕ヽ)')
                print('*:･ﾟ✧ ✧ﾟ･: * VITÓRIA DO JOGADOR !!! *:･ﾟ✧ ✧ﾟ･: *')
                print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧PARABÉNS✧ﾟ･: *ヽ(◕ヮ◕ヽ)')
                print('*:･ﾟ✧ ✧ﾟ･: *'*3)
                vitoria += 1
            else:
                print('VITÓRIA DO COMPUTADOR !!!')
                break
print('GAME OVER! \nVocê venceu {} vezes!'.format(vitoria))
print('=' * 45)
