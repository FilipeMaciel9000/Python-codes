n = int(input('Digite o numero que você deseja converter: '))
print('''Digite:
[1] Para converter o numéro para base BINÁRIA
[2] Para converter o numéro para base OCTAL
[3] Para converter o numéro para base HEXADECIMAL''')
x = int(input('-> '))
if x == 1:
    print('{} em Binário é {}'.format(n, bin(n)))
elif x == 2:
    print('{} em Binário é {}'.format(n, oct(n)))
elif x == 3:
    print('{} em Binário é {}'.format(n, hex(n)))
else:
    print('''Opção inválida. 
    Tente de novo; por favor''')