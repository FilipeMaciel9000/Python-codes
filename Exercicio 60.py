'''
Função: Esse programa recebe um números calcula o seu fatorial de três formas diferentes
Autor: Filipe Rios Mariz Maciel
Data: 26/06/2021
1) Usando bibliotecas:
2) [Exercicio 60.1]
3) Usando laço de repetição for [Exercicio 60.2]
'''
from math import factorial #(1)
print('Calculando o fatorial com a bibloteca MATH')
x = int(input('Digite o número que você quer fatorar: '))
f = factorial(x)
print('O fatorial de {} é {}'.format(x, f))


