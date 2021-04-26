#Primeiro e ultimo nome de alguem
nome=str(input('Por favor digite seu nome: ')).strip()
separa=nome.split()
print('Seu primeiro nome é {}'.format(separa[0].capitalize()))
print('Seu ultimo nome é {}'.format(separa[len(separa)-1].capitalize()))