salario = float(input('Digite o seu salário: '))
if salario <= 1250.00:
    novo = salario + (salario * (15/100))
else:
    novo = salario + (salario * (10 / 100))
print('Seu salário era de {}, a partir do ajuste seu salário será= {}!'.format(salario, novo))