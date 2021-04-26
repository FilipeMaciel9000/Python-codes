from datetime import date
data = date.today().year
print('*** FOLHA DE ALISTAMENTO MILITAR OBRIGATÓORIO ***')
nome = str(input('Digite seu nome: ')).capitalize()
sexo = str(input('Digite seu sexo: ')).capitalize()
nas = int(input('Digite seu ano de nascimento: '))
idade = data - nas
tempo = 18 - idade
print('''Olá {}; 
    Bem vindo a folha de alistamento militar obrigatório; 
    Se você nascem em {} hoje você tem ou vai fazer {} nesse ano.'''.format(nome, nas, idade))
if sexo == 'Masculino' and idade == 18:
    print('''Todo brasileiro do sexo masculino, no ano em que completa 18 anos, deve se alistar obrigatoriamente no Serviço Militar.
    Esse alistamento é obrigatório inclusive aos portadores de deficiência física e mental;
    Apresente-se na sua unidade de alistamento mais próxima se você ainda não fez.''')
elif sexo == 'Masculino' and idade >= 19 and idade <= 40:
    print('''Com {} anos você está na faixa etária mínima de 30 anos e máximo 40 anos de idade;
    Você pode se alistar mesmo não sendo mais obrigado.'''.format(idade))
elif sexo == 'Feminino':
    print('Seu sexo é feminino, por isso mesmo tendo 18 anos, você não é obrigada a se alistar no Serviço Militar.')
else:
    print('Ainda falta {} anos para você se alistar'.format(tempo))