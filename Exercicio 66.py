'''
@goal: Receber varios números, somar todos esses números e parar ao digitar 999;
@author: Filipe Rios Maciel Maciel
@date: 23/01/2022
@Declarations: Funciona mas tem muitos Problemas; como será que o professor respondeu?!
Como eu fiz:
1) As variaveis de contagem, de acumulo e que recebera os números começam com zero;
2) Loop enquanto a varial que recebera os números for diferente de 999 um número sera inserido;
3) A variavel de contagem conta cada número inserido;
4) A variavel de acumulo recebe cada número inserido;
5) Estrutura condicional, Se a varial que recebera os números for igual a 999:
6) Break comando para parar o loop <- comand break;
7) Mostra a variavel de contagem menos 1 e a variavel soma menos 999 formatados.
'''

cont = soma = n = 0  # 1
while n != 999:  # 2
    n = int(input('Digite um valor (999 para parar): '))
    cont += 1  # 3
    soma += n  # 4
    if n == 999:  # 5
        break  # 6
print('Foram digitados {} números e a soma entre esses numeros é {}'.format(cont - 1, soma - 999))  # 7
print('Acabou!')
