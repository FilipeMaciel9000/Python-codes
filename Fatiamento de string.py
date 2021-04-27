frase='Curso em Vídeo Python'
#Analise de string
print(len(frase))
# 'comprimento' da variavel frase, quantidade de caracteres na variavel frase (tipo string)
#Muito util pra saber qual é o tamanho da fase, isso vai facilitar o fatiamento.
print(frase.count('o'))
print(frase.count('o',0,19))
print(frase.find('urso'))
print(frase.find('PHP'))
print('Curso' in frase)
#Fatiamento de string
print(frase[:5])
print(frase[:8])
print(frase[:14])
print(frase[::])
print(frase[15:21])
print(frase[9:14])
print(frase[6:8])
print(frase[0:5])
print(frase[6:8])
print(frase[9:14])
print(frase[15:21])
#Pulando carcteres
print(frase[::2])
print(frase[9:21:3])
print(frase[9::1])
#Transformação de string
print(frase.replace('Python','PHP'))
print(frase.upper())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
#Divisão de string
print(frase.split())
#Junção de string
print('-'.join(frase))