'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from time import sleep
from random import randint
jogos = []
lista = []
quant = int(input('Quantos jogos deseja gerar: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        gerados = randint(1,60)
        if gerados not in lista:
            lista.append(gerados)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1    
for i, j in enumerate(jogos):
    print(f'\nJogo{i}: {j}', end=' ')