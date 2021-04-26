#Calculando descontos
x=float(input('Qual é o preço do produto? R$'))
a=x*0.05
b=x*0.1
c=x*0.15
d=x*0.25
e=x*0.5
print('Para um produto que custa {}R$ o abatimento será: \n {} com 5% de desconto; \n {} com 10% de desconto; \n {} com 15% de desconto; \n {} com 25% de desconto; \n {} com 50% de desconto.'.format(x,a,b,c,d,e))