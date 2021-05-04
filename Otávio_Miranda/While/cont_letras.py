'''Faça um programa que leia um palavra e conte quantas vezes a letra "A' aparece
e qual foi a letra que mais se repetiu e quantas vezes.'''

frase = 'carapicuibbbbbba'
quantidade = 0
cont = 0
maisvezes = ''
for f in frase:
    quantidade = frase.count(f)
    if quantidade > cont:
        cont = quantidade
        maisvezes = f
print(f'{cont}, {maisvezes}')
    


    
  

