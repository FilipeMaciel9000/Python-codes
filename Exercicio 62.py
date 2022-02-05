"""
Função: Esse programa mostra os 10 números de uma progressão Aritmética com estrutura while;
Autor: Filipe Rios Mariz Maciel
Data: 16/07/2021
Progressão Aritmética com python;
Uma progressão aritmética, nada mais é, do que uma contagem com um nome mais chique;
Porem ha uma variavel razão que vai definir de quanto em quanto se dara essa contagem;
Assim, Faça um programa que construa uma PA finita com 10 termos; assim como no exercicio anterior;
porém com a opção de deixar o usuario decidir se quer continuar e quais os numeros da sequencia mostrar apartir;
dos 10 primeiro termos
"""

print('=' * 65)
print('''
Uma Progressão aritimetica (PA) é dada da seguinte forma:
formula -> an=a1+(n-1)*r
Onde:
an -> Termo geral
a1 -> Primeiro termo da sequência
n -> Números de termos da PA ou posição do termo númerico da PA
r -> Razão da PA
Assim vamos colcular uma PA usando a estrutura while com python:
''')
print('=' * 65)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = primeiro_termo
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        c += 1
    print('BREAK')
    mais = int(input('Quantos termos a mais você quer mostrar> '))
print('FIM')
if mais == 0:
    print('Progreesão encerrada com {} termos mostrados'.format(total))
