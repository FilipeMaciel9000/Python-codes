# Desses trÊs numeros qual é o maior
a = int(input('Digite um número:= '))
b = int(input('Digite um número:= '))
c = int(input('Digite um número:= '))
menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
print('O menor valor digitado foi: {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O menor valor digitado foi: {}'.format(maior))
