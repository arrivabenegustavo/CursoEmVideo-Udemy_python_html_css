'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Sao Paulo','Thais','Casamento','Felicidade','Jordan')
for p in palavras:
    print(f'\nNa palavra {p} existem as vogais ',end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(v,end=' ')
  