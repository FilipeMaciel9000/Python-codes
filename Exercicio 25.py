#Tem Silva no seu nome
nome=str(input('Digite seu nome completo: ')).strip()
print('Tem Silva no seu nome?!')
if 'Silva' in nome.lower():
    print('Sim!')
else:
    print('Não!')