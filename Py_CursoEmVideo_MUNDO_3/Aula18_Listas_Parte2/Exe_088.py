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
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont == 6: # conta até 6, pis o jogos da mega sena são 6 número em cada jogo
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1 
print()
# este FOR mostra cada jogo em um linha
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)