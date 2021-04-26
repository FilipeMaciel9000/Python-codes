#Calculando reajuste salarial
x=float(input(' Quanto você ganha em R$ ? '))
y=float(input(' Quanto vai ser o aumento em % ? '))
a=x*(y/100)
r=a+x
print('O seu salario base é {};\n Seu reajuste será{};\n E seu novo salario sera{}'.format(x,a,r))