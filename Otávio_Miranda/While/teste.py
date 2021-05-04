frase = 'sao paulo futeeeeeebol clube'
maisvezes = ''
totalletra = 0
cont = 0
for letra in frase:
    totalletra = frase.count(letra)
    if totalletra > cont:
        cont = totalletra
        maisvezes = letra
print(f'{cont},{maisvezes.upper()}')

    