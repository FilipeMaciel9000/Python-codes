#Mostra um número real e imprima os n n primeiros números ímpares naturais.
n = int(input("Digite o valor de n: "))
i = 1
while i <= (n+n):
    if i%2!=0:
        print(i)
        i += 1
    else:
        i += 1
