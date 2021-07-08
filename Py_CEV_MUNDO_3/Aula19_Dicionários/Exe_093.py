''' Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
liga = {}
gols = []
totgol = 0
liga['jogador'] = input('Nome do Jogador: ')
jogos = int(input(f'Quantos jogos {liga["jogador"]} disputou: '))
for c in range(0, jogos):
    gols.append(int(input(f'Marcou quantos gols na partida {c+1}: ')))
    liga['gols'] = gols
liga['total'] = sum(gols) # SUM função de soma
print(30*'-')
print(liga)
print(30*'-')
for k, v in liga.items():
    print(f'O campo {k} tem valor o {v}')
print(30*'-')
print(f'O jogador {liga["jogador"]} jogou {jogos} partidas e balançou as redes {liga["total"]} vezes.\n')
for i, v in enumerate(gols):
    print(f'Na {i+1}ª partida marcou {v} vezes.')
       
