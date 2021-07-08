# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
números = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10),)
print(f'Os números sorteados foram:', end='') # fora do for para não repetir e mostrar os  números  na mesma linha
for n in números:
    print(f'{n}',end=' ') # para repetir os números na mesma linha
print(f'\nO maior número é {max(números)}') #max() para o maior número dentro da tupla
print(f'O menor número é {min(números)}')#min() menor número dentro da tupla


