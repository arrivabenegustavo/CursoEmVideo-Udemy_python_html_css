'''Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO. Desconsiderando os espaços.
Ex: Após a sopa / a sacada da casa / a torre da derrota / anotaram a data da maratona'''

frase = str(input('Digite uma frase: ')).split()
frase = ''.join(frase)
inverso = ''.join(frase[::-1])
if frase == inverso:
    print('È um PALÍNDROMO')
else:
    print('Não é um PALÍNDROMO')
    