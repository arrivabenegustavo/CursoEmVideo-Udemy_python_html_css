''' faça um programa que mostre na tela uma CONTAGEM REGRESSIVA
para o estouro de fogos de artifícios. indo de 10  até 0, com uma pausa de 1 segundo'''

from time import sleep
c = 0
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('POW POW POW\n')
sleep(1.5)
print('BUUUUMMMMM')
