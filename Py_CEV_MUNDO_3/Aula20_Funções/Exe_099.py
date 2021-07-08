'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(*num):
    maior = 0
    print('-'*30)
    print('Analisando os valore passados...')
    for i, c in enumerate(num):
        print(c,end=' ',flush=True)
        sleep(0.5)
        if i == 0 or maior < c:
            maior = c        
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')
                   
maior(3,6,2,1,9)
maior(8,1,9,10) 
maior(1,2,3)
maior(5, 2)
maior(8)
maior()