"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa;
Calcule seu Índice de Massa Corporal (IMC)
O resultado é dado em kg/m2
Mostrando seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""
x = float(input('Insira seu peso (não minta): '))
y = float(input('Insira sua altura (não minta): '))
imc = x/(y**2)
print('Com a altura {} m, o peso {} Kg, o seu IMC é de {:.2f} kg/m2'.format(y, x, imc))
print('SEGUNDO A TABELA DE IMC:')
print('=====' * 10)
print(" –> IMC abaixo de 18,5: Abaixo do Peso; \n –> Entre 18,5 e 25: Peso Ideal; \n –> 25 até 30: Sobrepeso; \n –> 30 "
      "até 40: Obesidade; \n –> Acima de 40: Obesidade Mórbida.")
print('=====' * 10)
if imc < 18.5:
    print('Você está: Abaixo do Peso!')
    print('-=-=-=-=-=-' * 2)
    print('Se cuida')
    print('-=-=-=-=-=-' * 2)
elif 18.5 <= imc < 25:
    print('*:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧ PARABÊNS *:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧')
    print('*:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧ Você está no peso ideal *:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧')
    print('*:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧ PARABÊNS *:･ﾟ✧ *:･ﾟ✧ *:･ﾟ✧')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso!')
    print('-=-=-=-=-=-' * 2)
    print('Se cuida')
    print('-=-=-=-=-=-' * 2)
elif 30 <= imc < 40:
    print('Você está obeso')
    print('-=-=-=-=-=-' * 2)
    print('Cuidado')
    print('-=-=-=-=-=-' * 2)
elif imc > 40:
    print('Você está com obesidade morbida')
    print('-=-=-=-=-=-' * 2)
    print('Cuidado')
    print('-=-=-=-=-=-' * 2)
