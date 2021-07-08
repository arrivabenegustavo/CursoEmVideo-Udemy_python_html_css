valores =list()
# valores inseridos na lista
#valores.append(2)
#valores.append(4)
#valores.append(8)

# Para que o usuário adicione valores a lista
for cont in range(0,5):
    valores.append(str(input('Digite uma palavra: ')))# repetirá 5 vezes
for p, c in enumerate(valores): # P -> posição / C -> conteúdo dentro da posição.
    print(f'Na posição {p} temos o valor {c.strip().title()}') # formata o conteúdo dentroo da lista