"""
Progressão Aritmética com python;
Uma progressão aritmética, nada mais é, do que uma contagem com um nome mais chique;
Porem ha uma variavel razão que vai definir de quanto em quanto se dara essa contagem;
Assim, Faça um programa que construa uma PA finita com 10 termos.
"""
print('='*40)
print('10 primeiros termos de uma PA')
print('='*40)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10-1) * r
for c in range(pt, decimo, r):
    print('{}'.format(c), end=' -> ')
print('Fim')