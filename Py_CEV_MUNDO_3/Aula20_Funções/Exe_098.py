'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep

def contagem(i, f, p):
    print('-'*30)
    print(f'Contagem de de {i} até {f}, de {p} em {p}')
    if p < 0: # caso o usuário coloque um número negativo
        p *= -1 # transforma em positivo, pois o segundo while o contador ja subtrai
    if i < f:
        cont = i
        while cont <= f:
            print(cont,end=' ',flush=True)  
            sleep(0.5)
            cont += p      
        print('Fim')              
    else:
        cont = i
        while cont > f:
            print(cont,end=' ',flush=True)
            sleep(0.5)
            cont -= p
        print('Fim')       
        print('-'*30)        
contagem(1, 10, 1)
contagem(10, 0, 2)
ini = int(input('Início: '))
fim = int(input(f'Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)