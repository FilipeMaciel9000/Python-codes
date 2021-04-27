print(' # '*10)
print(' # # # # # EL CAMINO # # # # # ')
print(' # '*10)
i = int(input("Digite o numéro de inicio: ")) # NUMÉRO ONDE A CONTAGEM COMEÇARA
f = int(input("Digite o numéro do fim: ")) # NUMÉRO ONDE A CONTAGEM TERMINARA
p = int(input("Digite o numéro de saltos: ")) # NUMÉRO PELO QUAL A CONTAGEM SERÁ FEITA
for c in range (i, f+1, p):
    print(c)