"""
Função: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
Autor: Filipe Rios Mariz Maciel
Data: 17/07/2021

"""
c = soma = media = maior = menor = 0
r = 'S'
while r in 'Ss':
    x = int(input('Digite um número: '))
    soma += x
    c += 1
    if x == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    r = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / c
print('Fim')
print('Você digitou {} números a media entre esses números é: {}'.format(c, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))