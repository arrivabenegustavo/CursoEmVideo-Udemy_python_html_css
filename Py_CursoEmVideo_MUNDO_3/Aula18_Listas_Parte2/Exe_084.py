'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas. 
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
 
cadastros = list()
pessoas = list()
opção = ' '
maior = menor = 0
while True:
    pessoas.append(input('Nome: '))
    pessoas.append(float(input('Peso: ')))
    if len(cadastros) == 0:
    # isto é, como LEN ainda é 0, quer dizer que ainda não tem nenhum cadastro dentro da lista
    # para que no inicio do programa,as variáveis recebam o mesmo valor.
    # este é o motivo do IF estar antes dos dados entrarem na lista principal[cadastros]
        menor = maior = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    cadastros.append(pessoas[:])
    pessoas.clear()
    opção = input('Quer continuar? ')
    if opção in 'Nn':
        break
# Neste caso o LEN consegue substituir o contador, pois NOME E PESO representa "UM" cadastro.
# pois ocupa uma posição dentro da lista principal[Cadastro]
print(f'Foram cadastradas {len(cadastros)} pessoas.')  
print(f'O maior peso foi {maior}KG de',end=' ')         
for p in cadastros:
    if p[1] == maior:
        print(f'{p[0]}',end=', ')
print()
print(f'O menor peso foi {menor}KG de',end='')
for p in cadastros:
    if p[1] == menor:
        print(f'{p[0]}',end=', ')

        
        
        
        
     