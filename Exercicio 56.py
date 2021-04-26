somadasidade = 0
mediaidade = 0
idademaisvelho = 0
nomemaisvelho = ''
totmulhermenor = 0
for i in range(1, 5):
    print('---- {}º Pessoa ---'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somadasidade += idade
    if i == 1 and sexo in 'Mm':
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > idademaisvelho:
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 18:
        totmulhermenor += 1
mediaidade = somadasidade / 4
print('A média das idades é {}!'.format(mediaidade))
print('O total de mulheres menores de idade é {}!'.format(totmulhermenor))
print('O homem mais velho é {} com seus {} anos!'.format(nomemaisvelho, idademaisvelho))
