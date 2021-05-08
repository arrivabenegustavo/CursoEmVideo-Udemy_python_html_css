'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior.'''

from time import sleep
from random import randint

def sorteia(lista):
    cont = 1
    print(f'Sorteando 5 valores na lista: ',end='')
    for cont in range(0, 5):
        n = (randint(1,10))
        print(f'{n}',end=' ',flush=True)
        lista.append(n)
        sleep(0.5)
    print(' FIM!')
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor   
    print(f'Somando os valores pares da lista {sorteados} temos {soma}\n')
    
sorteados = list() 
sorteia(sorteados)
somaPar(sorteados)
       