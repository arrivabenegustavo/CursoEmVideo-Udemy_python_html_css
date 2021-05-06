'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

artilharia = []
jogador = {}
gol =  []
while True:
    jogador.clear() #limpa dado anterior
    jogador['nome'] =  input('Digite o nome do jogador: ').capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gol.clear() #limpar dado anterior
    for p in range(0, partidas):
        gol.append(int(input(f'Quantos gols marcou na {p+1}ª partida: ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol) # soma  os gols dentro da lista GOL
    artilharia.append(jogador.copy())
    while True:
        print('-'*30)
        opcao = input('Deseja continuar [S/N]: ').upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Porfavor, digite S ou N.')
    print('-'*30)
    if opcao == 'N':
        break
print('*'*40)
print('Cod ',end='')
for k in jogador.keys(): #Para mostrar a chaves dos dicionários('nome', 'gols'..etc)
    print(f'{k:<15}',end='')
print()# nesse caso quebra a linha pra mantes o dados na mesma linha
for i, v in enumerate(artilharia):# para usar o contador (i) do enumerate
    print(f'{i:^3} ',end='')
    for d in v.values(): # para mostrar apenas os valores dentro dos dicionários
        print(f'{str(d):<15}',end='') #por conter números, é necessário a conversão dos valores para (str)
    print()
while True:
    print('-'*40)
    ver = int(input('Mostrar dados de qual jogador? ou (999) para sair: '))
    print('-'*40)
    if ver == 999:
        print('\n>>>> PROGRAMA FINALIZADO <<<<\n')
        break
    if ver >= len(artilharia):
        print('ERRO! Não existe jogador com código 5.\nPor favor, digite um número até {len(artilharia)}')
    else:
        print(f'--LEVANTAMENTO do jogador {jogador["nome"]}:')    
        for p, g in enumerate(artilharia[ver]['gols']):
            print(f'     Na {p+1}ª partida marcou {g} vezes.')    
    
           
            
        
        
    
           
    
        
       


    
    