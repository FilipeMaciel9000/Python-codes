cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30;40m',
         'pretoecinza': '\033[7:30m',
         'matrix': '\33[0;32;40m',
         'rubronegro': '\33[0;31;40m', }
nome=input('Por favor digite seu nome: ')
print('Oi {}{}{}! Muito prazer'.format(cores['verde'], nome, cores['limpa']))
