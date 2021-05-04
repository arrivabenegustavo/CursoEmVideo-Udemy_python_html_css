# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
números = []
for c in range (1, 6):
    n = int(input(f'digite o {c}º número: '))
    if c == 1 or n > números[-1]:
        números.append(n)
        print('Número inserido no final')
    else:
        for posição, elemento in enumerate(números):
            if n <= elemento:
                números.insert(posição, n)
                print('Número inserido')
                break
            
print(f'{números}')