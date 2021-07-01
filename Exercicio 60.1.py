'''
Função: Esse programa recebe um números calcula o seu fatorial de três formas diferentes
Autor: Filipe Rios Mariz Maciel
Data: 26/06/2021
1) Usando bibliotecas [Exercicio 60]
2) Usando laço de repetição e estrutura condicional:
3) Usando laço de repetição for [Exercicio 60.2]
'''
x = int(input('Insira o número que será fatorado: '))
c = x
f = 1
print('Calculando {}! '.format(x))
while c > 0:
    print('{}'.format(c), end=' ')
    print('*' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)
