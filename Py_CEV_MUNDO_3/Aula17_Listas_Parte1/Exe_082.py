# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    # a resolução de pares e impares pode ser feito dessa maneira cometada abaixo
    '''if n % 2 == 0:
        par.append(n) 
    else:    
        impar.append(n)'''
    # ou com o FOR na linha 21
    # se optar pelo For, da tbm para alterar o recebimento dos números para lista.append(int(input.......))
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar: ')).strip().upper()[0]
    if opção == 'N':
       break
# varre a posição 'i' ate´encontrar um valor 'v' que valide os Ifs abaixo
for v in lista: 
    if v % 2 == 0:
         par.append(v)
    else:
        impar.append(v)    
print(f'A lista completa é {lista}') 
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')    



    
  
    