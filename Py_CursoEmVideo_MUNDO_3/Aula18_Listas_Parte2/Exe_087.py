'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = soma_coluna3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o número na posição {l}, {c}: '))                                   
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print()
print('-'*30)
print(f'A soma dos números pares foi {soma_par}')
for l in range(0,3):
    soma_coluna3 += matriz[l][2] 
# para somar a 3ª coluna, foi necessário um FOR para varrer as linha e manter a coluna (MATRIZ[l][2]ultima  coluna)
print(f'A soma dos números da 3ª coluna foi {soma_coluna3}')
for c in range(0, 3): # Para varrer os valores da coluna e mater a linha
    # c == 0 -> na primeira contagem MAIOR j recebe o primeiro valor da linha
    # matriz[1][c] -> começa a comparar se o número dentro de MAIOR é maior que o número na posição da matriz[1][c]
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]          
print(f'O maior valor da 2ª linha foi {maior}')


       
        