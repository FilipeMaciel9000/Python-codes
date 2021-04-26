#Cortando os digitos de um número
x=int(input('Digite um número, qualque número: '))
u=x//1%10
d=x//10%10
c=x//100%10
m=x//1000%10
print('Analisando . . . o número {}'.format(x))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))