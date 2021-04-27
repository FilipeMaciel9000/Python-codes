n=int(input("digite um número inteiro:"))
i = 2
while i<n:
    if n%i == 0:
        verify= 0
        i=n
    else:
        i=i+1
        verify=1
if verify==1 or n==2:
    print("primo")
else:
    print("não primo")
