#Calcular quanto de tinta é necessario pra pintar uma parede e mostrar as dimenções dessa parede
l=float(input('Qual é a largura da parede que será pintada? '))
a=float(input('Qual é a altura da parede que será pintada? '))
ar=l*a
t=ar/2
print('As dimenções da sua parede são de {}x{}m² e sua área é de {}m² '.format(l,a,ar))
print('Para pintar essa parede você precisa de {}L de tinta'.format(t))
