'''
Função: Esse programa recebe dois números e realiza uma das operações matemáticas disponibilizadas
Autor: Filipe Rios Mariz Maciel
Data: 25/06/2021
1) pega os dois valores
2) Essa variável é referente a um dos valores de opções que vão controlar o loop e as estruturas condicionais
3) Enquanto o usuário inserir um valor menor que 7 é programa não vai parar a execução
4) Recebe um valor inteiro correspondente a uma das opções do painel
5) A estrutura condicional fará as operações matemáticas de acordo com o que o usuário digitar
6) Eu poderia ter declarado uma variável soma; mas preferi fazer a operação diretamente pelo Format que vai jogar o resultado dentro das chaves
7) Na divisão declarei duas variáveis porque quis mostrar os resultados de x/y e y/x
8) Formatação para apenas duas casas depois da virgula {:.2f}
9) Uma forma alternativa de achar raiz quadrada é elevar um número a potências 1/2
10) Mostrara a mensagem de opção invalida se o usuário resolver botar qualquer opção que não está na tabela
'''


print('-=-=-=-=-'*10)
x = float(input('>>> Digite o primeiro número: ')) #(1)
y = float(input('>>> Digite o segundo número: '))

op = 0 #(2)
while op != 7: #(3)
    print('>>> Digite uma das opções disponíveis para executar o programa: \n')
    print('''
    >>> [1] Opção: Somar os dois números
    >>> [2] Opção: Subtrair os dois números
    >>> [3] Opção: multiplicar os dois números
    >>> [4] Opção: dividir os dois números
    >>> [5] Opção: Raiz quadrada dos dois números
    >>> [6] Opção: Elevar os números ao quadrado
    >>> [7] Opção: Encerrar programa
    ''')
    print('-=-=-=-=-' * 10)
    op = int(input('>>> Qual é a sua escolha? '))#(4)
    if op == 1:#(5)
        print('>>> A soma dos números inserido é {}'.format(x + y))#(6)
    elif op == 2:
        print('>>> A subtração dos números inserido é {}'.format(x - y))
    elif op == 3:
        print('>>> A multiplicação dos números inserido é {}'.format(x * y))
    elif op == 4:
        d1 = x / y #(7)
        d2 = y / x
        print('>>> A divisão de {} por {} é {:.2f}'.format(x, y, d1))#(8)
        print('>>> A divisão de {} por {} é {:.2f}'.format(y, x, d2))
    elif op == 5:
        print('>>> A raiz quadrada de {} é {}'.format(x, x ** (1 / 2)))#(9)
        print('>>> A raiz quadrada de {} é {}'.format(y, y ** (1 / 2)))
    elif op == 6:
        print('>>> {} ao quadrado é {}'.format(x, x**2))
        print('>>> {} ao quadrado é {}'.format(y, y**2))
    else:
        print('>>> Opção invalida; \n Digite o números de uma das opções do painel!')#(10)
    print('-=-=-=-=-'*10)
print('>>> Programa encerrado!')
