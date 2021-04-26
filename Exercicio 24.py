# Essa cidade começa com nome de santo?
cidade = input('Digite o nome da sua cidade: ').strip()
if "Santo" in cidade:
    print('Sua cidade tem nome de santo')
elif 'São' in cidade:
    print('Sua cidade tem nome de santo só que com São')
else:
    print('Sua cidade não começa com nome de santo')