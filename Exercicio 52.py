"""

Números primos;
Um número primo só divisível por um e por ele mesmo.
Faça um programa que identifique a quantidade de números pelos quais ele é divisível;
E mostre uma mensagem se esse número é ou não é primo.

"""
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30;40m',
         'pretoecinza': '\033[7:30m',
         'matrix': '\33[0;32;40m',
         'rubronegro': '\33[0;31;40m', }
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=" ")
        tot += 1

    else:
        print('\033[31m', end=" ")
    print('{}'.format(c), end='')
print('\n\033[mO número {} é divisivel {} vezes (números em azul)'.format(n, tot))
if tot==2:
    print('Por isso o número {} É PRIMO'.format(n))
else:
    print('\033[mPor isso {} NÃO É PRIMO'.format(n))
