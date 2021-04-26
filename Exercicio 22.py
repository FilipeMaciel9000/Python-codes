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
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
#Divisão de string
print(frase.split())
#Junção de string
print('-'.join(frase))

#Pratica
x=str('Curso em Vídeo python')
print(len(x))
print(x[:5])
print(x[9])
print(x[9:13])
print(x[9:21])
print(x[9:21:2])
print(x[:5])
print(x[15:])
print(x[:])
print(x[9:3])
print(x.count('o'))
print(x.count('o',0,13))
print(x.find('deo'))
print(x.find('Android'))
print('Curso' in x)
print(x.replace('Python','RPG'))
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.strip())
print(x.rstrip())
print(x.lstrip())
print(x.split())
print('~'.join(x))

y=str('     Aprendendo Python    ')
print(y.strip())
print(y.rstrip())
print(y.lstrip())
print(y.split())
print('='.join(y))

texto=str(""" O vídeo fornece uma maneira poderosa de ajudá-lo a provar seu argumento. 
Ao clicar em Vídeo Online, você pode colar o código de inserção do vídeo que deseja adicionar. 
Você também pode digitar uma palavra-chave para pesquisar online o vídeo mais adequado ao seu documento. 
Para dar ao documento uma aparência profissional, o Word fornece designs de cabeçalho, rodapé, folha de rosto e caixa de texto que se complementam entre si. 
Por exemplo, você pode adicionar uma folha de rosto, um cabeçalho e uma barra lateral correspondentes.
Clique em Inserir e escolha os elementos desejados nas diferentes galerias. 
Temas e estilos também ajudam a manter seu documento coordenado. 
Quando você clica em Design e escolhe um novo tema, as imagens, gráficos e elementos gráficos SmartArt são alterados para corresponder ao novo tema. 
Quando você aplica estilos, os títulos são alterados para coincidir com o novo tema. 
Economize tempo no Word com novos botões que são mostrados no local em que você precisa deles.""")
print(texto[:])
print('^'.join(texto))
print(texto.strip())
print(len(texto))
print(texto.find('deo'))
print(texto.find('cu'))
print(texto.count('o',0,33))
print(texto.find('texto'))
print(texto.find('Voadora'))
print('Curso' in texto)
print('Chupadinha' in texto)
print('Design' in texto)
print('documento' in texto)
print(texto.count('o'))
print(texto[9:3])
print(texto[:31:5])
print(texto[13::4])
print(texto[::2])
