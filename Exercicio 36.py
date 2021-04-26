from time import sleep
x=float(input('Insira o valor da casa: '))
y=float(input('Insira seu salário: '))
z=int(input('Em quantos anos você ira pagar pelo imóvel: '))
limite=y*0.3
pgto= x/(z*12)
print('Para pagar uma casa de R${:.2f} em {} anos '.format(x, z))
print('A prestação será {:.2f}'.format(pgto))
print('Comparando as prestações da casa de R${:.2f} e seu valor mínimo de R${:.2f}'.format(pgto, limite))
print('Processando resultado . . .')
sleep(2)
if pgto <= limite:
    print('Empréstimo: APROVADO')
else:
    print('Empréstimo: NEGADO')