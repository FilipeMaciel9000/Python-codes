#Ano bissesto:
from datetime import date
ano = int(input(" Vamos ver se um ano é bissexto ou não é!\n Digite 1 para analisar o ano atual; \n Ou\n Digite o ano "
                "que você quer analisar: "))
if ano == 1:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))
