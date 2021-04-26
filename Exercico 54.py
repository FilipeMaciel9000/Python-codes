from datetime import date

atual = date.today().year
ma = 0
me = 0
for c in range(1, 8):
    ano = int(input('Participante número {}º\nPor favor; Digite o ano do seu nascimento: '.format(c)))
    idade = atual - ano
    if idade >= 18:
        ma += 1
    else:
        me += 1
print('Total dos participantes maiores de idade: {}\nTotal dos participantes menores de idade: {}'.format(ma, me))
