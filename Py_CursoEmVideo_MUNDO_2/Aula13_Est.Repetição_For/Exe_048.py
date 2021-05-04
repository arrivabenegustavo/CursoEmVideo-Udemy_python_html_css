'''Faça um programa que calcule a SOMA entre todos os NÚMEROS IMPARES 
que são MÚLTIPLOS DE TRÊS e que se encontram no intervalo de 1 até 500.'''
c = 0
soma = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
print(soma)        
