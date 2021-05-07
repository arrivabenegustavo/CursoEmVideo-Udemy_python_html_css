'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

artilharia = []
jogador = {}
gol = []
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    gol.clear()
    for p in range(partidas):
        gol.append(int(input(f'Quantos gols foram marcados na {p+1} partida? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    artilharia.append(jogador.copy())
    while True:
        opcao = input('Deseja continuar [S/N]: ').upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Por favor, digite S ou N.')
    if opcao == 'N':
        break
print('*'*30)
print('Cod ',end='')
for k in jogador.keys():
    print(f'{k:<15}',end='')
print()
for c, v in enumerate(artilharia):
    print(f'{c:^3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
while True:
    ver = int(input('Deseja consultar qual jogador? 999 para sair: '))
    if ver == 999:
        break
    if ver >= len(artilharia):
        print(f'ERRO! O código {ver} não existe!')
    else:
        print(f'--LEVANTAMENTO do jogador {artilharia[ver]["nome"]}:')
        for p, g in enumerate(artilharia[ver]['gols']):
            print(f'   Na {p+1}ª partida marcou {g} gols')
            
        
            
    
           
            
        
        
    
           
    
        
       


    
    