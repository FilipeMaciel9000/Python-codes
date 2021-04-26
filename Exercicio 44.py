"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto;
Considerando o seu preço normal e condição de pagamento:
– à vista dinheiro
- cheque: 10% de desconto
– cartão:
- à vista : 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'azul': '\033[34m',
         'ciano': '\033[36m',
         'lilas': '\033[35m',
         'preto': '\033[30m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30;40m',
         'pretoecinza': '\033[7:30m',
         'matrix': '\33[0;32;40m',
         'rubronegro': '\33[0;31;40m',
         'azulepreto': '\33[7;30;44m'}

print('===== LOJÃO DE BUENAS =====')
preso = float(input("Insira o preço das suas compras: "))
print('=====' * 10)
print('''Formas de pagamento:
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
print('=====' * 10)
opcao = int(input('Digite o numéro da sua forma de pagamento: '))
if opcao == 1:
    total1 = preso - (preso * (10 / 100))
    print('=====' * 10)
    print('Você têm 10% de desconto nessa opção; o preço do seu desconto será {:.1f}R$; o preço atual do seu produto '
          'é {:.1f}R$'.format(preso * (10 / 100), total1))
    print('Obrigado pela preferência; volte sempre!')
    print('=====' * 10)
elif opcao == 2:
    total2 = preso - (preso * (5 / 100))
    print('=====' * 10)
    print('Você têm 5% de desconto nessa opção; o preço do seu desconto será {:.1f}R$; o preço atual do seu produto é '
          '{:.1f}R$'.format(preso * (5 / 100), total2 / 2))
    print('Obrigado pela preferência; volte sempre!')
    print('=====' * 10)
elif opcao == 3:
    total3 = preso
    parcela = total3 / 2
    print('=====' * 10)
    print('o preço do seu produto será pago em 2x de {:.1f}R$ sem juros'.format(parcela))
    print('O valor que você vai pagar no final será {:.1f}R$'.format(preso))
    print('Obrigado pela preferência; volte sempre!')
    print('=====' * 10)
elif opcao == 4:
    totpar = int(input('Digite a quantidade de pracelas: '))
    total4 = preso + (preso * (20 / 100))
    parcela = total4 / totpar
    print('=====' * 10)
    print('Você têm 20% de juros nessa opção;')
    print('Com os juros seu de {:.1f}R$ ficara por {:1f}R$'.format(preso, total4))
    print('Você escolheu pagar {:.1f}x de {:.1f}R$'.format(totpar, parcela))
    print('Obrigado pela preferência; volte sempre!')
    print('=====' * 10)
else:
    print('{}OPÇÃO INVALIDA{}'.format(cores['vermelho'], cores['limpa']))
    print('Por favor; tente novamente')
