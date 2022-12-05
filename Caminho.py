print(' # '*10)
print(' # # # # # EL CAMINO # # # # # ')
print(' # '*10)
i = int(input("Digite o numéro de inicio: ")) # NUMÉRO ONDE A CONTAGEM COMEÇARA
f = int(input("Digite o numéro do fim: ")) # NUMÉRO ONDE A CONTAGEM TERMINARA
s = int(input("Digite o numéro de saltos: ")) # NUMÉRO PELO QUAL A CONTAGEM SERÁ FEITA
for i in range (i, f+1, s):
    print(i)
