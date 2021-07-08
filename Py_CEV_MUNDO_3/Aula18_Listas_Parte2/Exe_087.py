'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = somac3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor na posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()# Após os laços do FOR c este print quebra pra linha de baixo, e assim até acabar os laços l
print('-'*30)    
print(f'A soma dos valores pares foi {somapar}')  
for l in range(0, 3):
    somac3 += matriz[l][2]
print(f'A soma dos valores na terceira coluna foi {somac3}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor na segunda linha foi {maior}')


       
        