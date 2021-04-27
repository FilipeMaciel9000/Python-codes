n = int(input("Digite um número inteiro: "))
s=0
while (n>0):
    s += n % 10
    n //= 10
print(s)
