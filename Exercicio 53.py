"""

"""
from time import sleep
frase = str(input('Digite algo: ')).upper().strip()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''
for letra in range(len(juntas) - 1, -1, -1):
    inverso += juntas[letra]
print('Analisando . . .')
sleep(3)

print('{} de trás pra frente é {}'.format(juntas, inverso))
print('. . .')
sleep(2)
print('. . .')
sleep(1)
print('Por isso {} é: '.format(frase).upper().strip())
if inverso == juntas:
    print('UM POLÍNDROMO')
else:
    print('NÃO É UM POLÍNDROMO')
