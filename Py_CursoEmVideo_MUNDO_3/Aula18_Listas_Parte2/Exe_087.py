'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = somac3 = maior = 0
# FOR para receber os valores
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}]: '))
# FOR para mostrar os valores recebidos
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
        if matriz[l][c] % 2 == 0: # soma os pares dentro da MATRIZ
            somapar += matriz[l][c]
    print()# para quebrar a linha ( 3 linhas com 3 colunas)
print('-'*30)
print(f'A soma dos valores pares foi {somapar}')
for l in range(0, 3): # varre as linhas
    somac3 += matriz[l][2] # varre as linhas[l] e congela a coluna[2]
print(f'A soma dos valores da terceira coluna foi {somac3}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha foi {maior}')
        


       
        