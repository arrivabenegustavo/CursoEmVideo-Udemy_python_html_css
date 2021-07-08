'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
dado = {'jogador1': randint(1,6), 'jogador2': randint(1,6),
        'jogador3': randint(1,6), 'jogador4': randint(1,6)}
ranking = []
for k, v in dado.items():
    print(f'O {k} tiroi {v} no dado.')
    sleep(1)
# lista recebe o dicionário na ordem(sorted) decrescente(reverse=true) pela função ITEMGETTER(que coloca na ordem pelo valor) 
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('-'*20)
print(f'{"RANKING":^20}')
for i, v in enumerate(ranking):
    print(f'{i+1}º {v[0]} com {v[1]} no dado.')