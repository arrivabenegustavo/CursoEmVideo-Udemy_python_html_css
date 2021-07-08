'''desenvolva um programa  que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles
que forem PARES. Se o valor o valor digitado for ÍMPAR desconsidera-lo.'''
soma = 0
for c in range (1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares foi de {soma}')