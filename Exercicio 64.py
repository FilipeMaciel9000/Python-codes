"""
Função: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
Autor: Filipe Rios Mariz Maciel
Data: 16/07/2021
"""
c = n = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números a soma entre eles é: {}'.format(c,soma))

