#cid = str(input("Em que cidade vc nasceu: ")).strip().title()
#print('Santo' in cid) # Operador in -> para dizer se X existe dentro da variável
#ou neste caso em qualquer lugar que a palavra Santo esteja, será verdadeiro
# no exemplo abaixo será verdadeiro apenas se estiver no começo

cid = str(input('Em que cidade vc nasceu: ')).strip()
print(cid[:5].title() == 'Santo') # Se a palavra estiver no começo da variável
