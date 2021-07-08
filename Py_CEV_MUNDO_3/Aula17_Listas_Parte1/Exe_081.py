# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista. 
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar [S/N]: ')).strip().upper()
    if opção == 'N':
        break
lista.sort(reverse=True)
print(f'\nTotal de {len(lista)} números digitados.')
print(f'A lista ordenada de forma decrescente é {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista\n')
else:
    print('O número 5 não foi encontrado na lista\n')
        
    