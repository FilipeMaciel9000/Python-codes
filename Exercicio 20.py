from random import shuffle
n1=input("Candidato: ")
n2=input("Candidato: ")
n3=input("Candidato: ")
n4=input("Candidato: ")
n5=input("Candidato: ")
lista=[n1, n2,n3,n4,n5]
shuffle(lista)
print('A ordem apresentada será: \n{} '.format(lista))
