#Escreva  um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.
i=1
f=1
n=int(input(' Digite o valor de n que será fatorado: '))
while i<=n:
    f=f*i
    i=i+1
print(f)
