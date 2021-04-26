#Faça converção de medidas
m=float(input('Digite o valor em metros que será convertido: '))
print(m)
mm=m*1000
cm=m*100
dm=m*10
dem=m*0.1
hm=m*0.01
km=m*0.001
print('{} em metros corresponde a:\n{} milímetros \n{} centímetros \n{} decímetros \n{} decômetros \n{} hectômetro \n{} quilômetros!'.format(m,mm,cm,dm,dem,hm,km))
