'''Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''

parimp = [[] , []]
for c in range(1,8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        parimp[0].append(n)
    else:
        parimp[1].append(n)  
parimp[0].sort()
parimp[1].sort()
print(f'Os números pares são {parimp[0]}')
print(f'Os números ímpares são {parimp[1]}')