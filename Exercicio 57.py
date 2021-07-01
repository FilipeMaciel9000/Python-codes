sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
print(sexo)
while sexo not in "MmFf":
    sexo = str(input('Opção invalida! \n Informe seu sexo [M/F]: ')).strip().upper()[0]
print('Seu sexo: {} foi cadastrado com sucesso'.format(sexo))