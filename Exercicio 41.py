from datetime import date

data = date.today().year
nome = str(input('Insira seu nome: ')).capitalize()
sexo = str(input('Insira seu sexo: ')).capitalize()
ano = int(input('Insira seu ano de narcimento: '))
idade = data - ano
print('Dados do atleta nadador:\n'
      'Nome: {}\n'
      'Sexo: {}\n'
      'idade: {}\n'
      'Você foi registrado na categoria: '.format(nome, sexo, idade))
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 25:
    print('Sênior')
else:
    print('Master')
