"""
Função: Esse programa mostra os primeiros números da Sequência de Fibonacci com estrutura while em python;;
Autor: Filipe Rios Mariz Maciel
Data: 16/07/2021
"""
primeiro_termo = 0
segundo_termo = 1
limite = int(input('Digite a quantidade de números que você quer ver da Sequência de Fibonacci: '))
print('{} -> {} -> '.format(primeiro_termo, segundo_termo), end='')
cont = 3
while cont <= limite:
   xtermo = primeiro_termo + segundo_termo
   primeiro_termo = segundo_termo
   segundo_termo = xtermo
   cont += 1
   print(' {} ->'.format(xtermo), end='')
print(' FIM')
if cont == limite:
    print('Esses são os {} termos da Sequência de Fibonacci'.format(limite))
