"""
# Meta dados:
    Autor: Filipe Rios Mariz Maciel
    Data: 23/04/2021
# Sobre o codigo:
  Gera uma senha com números, letras minúsculas, letras maiusculas e simbolos;
  Coloque '#' antes de +string. pra tirar atributos da sua senha:
  string.digits + string.ascii_lowercase + string.ascii_uppercase (Ou só
  string.ascii_letters pra ser menos especifico) + string.punctuation.
# Bibliotecas usadas:
  Foram usadas as bibliotecas;
  random para escolha dos caracteres;
  string para uso dos caracteres;
  sys para parar o programa se o usuario escolher uma opção invalida;
  E time só para dar um charme no programa.
#Variaveis usadas:
  Variavel tamanho define a quantidade de digitos da senha
  Variavel op
"""
from random import choice
from time import sleep
import string
import sys
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30;40m',
         'pretoecinza': '\033[7:30m',
         'matrix': '\33[0;32;40m',
         'rubronegro': '\33[0;31;40m', }
print('-=-' * 30)
print('{} TOP {} {} SECRET {}'.format(cores['verde'], cores['limpa'], cores['verde'], cores['limpa']))
print('-=-' * 30)
print('\033[32m Bem vindo ao serviço secreto de senhas de segura máxima; \033[m')
print('''\033[32m Opções de serviço:
 [1] Senha somente com letras;
 [2] Senha com números e letras;
 [3] Senha com números, letras e símbolos. \033[m''')
print('-=-' * 30)
op = int(input('\033[32m Escolha uma das três opções: \033[m'))
tamanho = int(input('''\033[32m Escolha a quantidade de caracteres da senha \n Obs: recomendado um mínimo de até 12 caracteres para uma senha forte: \033[m'''))
print('-=-' * 30)
valores1 = string.ascii_letters
valores2 = string.ascii_letters + string.digits
valores3 = string.ascii_letters + string.digits + string.punctuation
senha = ''
for i in range(tamanho):
    if op == 1:
        senha += choice(valores1)
    elif op == 2:
        senha += choice(valores2)
    elif op == 3:
        senha += choice(valores3)
    else:
        sleep(5)
        print('\033[31m ERROR \033[m')
        print('''\033[32m Escolha uma das três opções de serviço disponíveis; \n E tente novamente! \033[m''')
        sys.exit()
print('\033[32m Processando . . .\033[m')
print('-=-' * 30)
sleep(2)
print('\033[32m A senha é: \033[m')
print('\033[31m', senha, '\033[m')
print('-=-' * 30)
sleep(1)
print('{} Sua senha foi criada com sucesso;{}'.format(cores['verde'], cores['limpa']))
print('{} Decore ou guarde em lugar seguro {}'.format(cores['verde'], cores['limpa']))
print('-=-' * 30)
sleep(1)
print('{} Este programa irá se autodestruir!{}'.format(cores['vermelho'], cores['limpa']))
print('-=-' * 30)
