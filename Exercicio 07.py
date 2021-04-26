#Faça a media aritimetica
n1=float(input('A primeira nota foi: '))
n2=float(input("A segunda nota foi: "))
m=(n1+n2)/2
print('A sua nota no primeiro semestre foi {:.1f}; sua nota no segundo semestre foi {:.1f}, assim a media das suas notas é {:.1f}'.format(n1, n2, m))#Aquela formatação dentro das chaves vai deixar apenas 1 casa depois da virgula.
if m>=7:
	print('Você já está de ferias. Parabêns!')
else:
    print('Você vai ter que fazer recuperação!')
