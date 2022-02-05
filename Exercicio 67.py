"""
@goal: programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
        O programa será interrompido quando o número solicitado for negativo;
@author: Filipe Rios Maciel Maciel
@date: 23/01/2022
@Declarations:
"""
n = 0
while True:
    n = int(input('Digite o número da tabuada que você quer estudar: '))
    print('=' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('=' * 30)
print('''Obrigado por usar o meu programa;
Bons estudos;
Volte sempre!
;]
''')
