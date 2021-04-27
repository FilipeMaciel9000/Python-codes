cores = {'limpa': '\033[m',
         'subilinhado': '\033[4m',
         'negrito': '\033[1m',
         'verde': '\033[32m',
         'preto': '\033[30m',
         'cinza': '\033[37m',
         'azul': '\033[34m',
         'ciano': '\033[36m',
         'lilas': '\033[35m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'negativo': '\033[7m',
         'pretoecinza': '\033[7:30m',
         'matrix': '\33[1;32;40m',
         'rubronegro': '\33[0;31;40m',
         'azulepreto': '\33[7;30;44m'}
print('{}Olá mundo;{}\n{}Pronto me livrei da maldição;{}\n{}Agorara posso aprender python despreocupado.{}'.format(
    cores['matrix'], cores['limpa'], cores['matrix'], cores['limpa'], cores['matrix'], cores['limpa']))
