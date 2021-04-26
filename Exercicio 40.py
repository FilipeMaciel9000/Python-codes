from time import sleep
n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
m=(n1+n2)/2
print('''No primeiro semestre sua nota foi {};
    No segundo semestre sua nota foi {};
    Com essas notas sua media fica {}'''.format(n1, n2, m))
print('Sua situação academica é: ')
sleep(2)
if m > 7:
    print('APROVADO')
elif 7 > m >= 5:
    print('RECUPERAÇÃO')
elif m < 5:
    print('REPROVADO')