#Isso pode formar um triangulo?!
print('###'*20)
print('= A N A L I S A D O R = D E = T R I Â N G U L O S =')
print('###'*20)
l1 = float(input('Digite o primeiro segmento: '))
l2 = float(input('Digite o segundo segmento: '))
l3 = float(input('Digite o terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 +l1:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')
