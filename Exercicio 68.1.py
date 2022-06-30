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
(1) Bibliotecas usadas: RANDOM para tornar aleatoria a escolha do computador.
                        TIME para fazer o programa falar pedra, papel, tesoura.
(2) Variaveis de contagem começam com zero;
(3) Variável jogador começa com uma string vazia;
(4) Variável continuar começa com S(sim) porque se o usuário obri o progrma subentende-se que ele quer começar a jogar;
(5) Opções de jogadas possiveis para o computador;
(6) Enfeite pra deichar o codigo bonito no final;
(7) Estrutura de repetição While que faz o codigo rodar enquanto o usuario digitar N para parar;
(8) Estrutura de repetição For que faz as três jogadas do jogo;
(9) Estruturas condicionais que definem o destino do jogo;
(10) Se continuar (7) for diferente de S o programa encerra mostrando o  resultado do jogo;
(11) Mostra o resultado do jogo;
"""
# (1)
from random import choice
from time import sleep

vitoria = 0  # (2)
derrota = 0
empate = 0
jogador = ' '  # (3)
continuar = 'S' # (4)
opcoes = ['pedra', 'papel', 'tesoura']  # (5)
print('=' * 50) # (6)
while continuar == 'S': # (7)
    for v in range(1, 4):  # (8)
        print('Vamos jogar pedra, papel, tesoura!') 
        jogador = str(input('Digite pedra, papel ou tesoura para jogar: ')) 
        computador = choice(opcoes)
        sleep(1)
        print('Pedra')
        sleep(1)
        print('Papel')
        sleep(1)
        print('Tesoura')
        if jogador == "pedra" and computador == 'pedra': # (9)
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
    if continuar == 'N': #(10)
        break
print('Fim de jogo!')
print('Você ganhou {} vezes; \nEmpatou {} vezes! \nE o computador ganhou {} vezes!'.format(vitoria, empate, derrota)) #(11)
if vitoria > derrota:
    print('*:･ﾟ✧ ✧ﾟ･: * VITÓRIA DO JOGADOR !!! *:･ﾟ✧ ✧ﾟ･: *')
else:
    print('Vitória do computador!')
print('=' * 50)
