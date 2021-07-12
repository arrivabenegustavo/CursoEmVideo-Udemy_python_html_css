# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
soma = cont = 0
print('*'*20)
print('JOGO DO PAR OU ÍMPAR')
print('*'*20)
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0,11) # precisa estar dentro do laço para sempre mudar o número
    soma = jogador + computador
    escolha = ' ' # precisa estar dentro do primeiro laço, para sempre perguntar Par ou Ímpar
    #Se ESCOLHA estiver fora do primeiro laço, o programa só perguntará Par ou Ímpar somente na primeira passagem
    while escolha not in 'PI':# Enquanto não for P ou I, não sairá do laço
        escolha = str(input('PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    print(f'Você escolheu {jogador} e computador {computador} > Total {soma}',end=' ')
    print('deu PAR' if soma % 2 == 0 else 'deu ÍMPAR') # acrescenta a classificação na frase a cima   
    print('-'*45)
    if soma%2==0: #Se soma for PAR
        if escolha == 'P':
            cont += 1 # conta toda vez que ganhar com PAR
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break 
    elif soma%2==1: # se soma for ÍMPAR
        if escolha == 'I':
            cont += 1 # conta toda vez que ganhar com ÍMPAR
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('-'*20)    
    print('Vamos jogar novamente!\n') 
print('-'*50)
print(f'GAME OVER! Você conseguiu vencer {cont} vezes!')    
print('-'*50)           
print('JOGO ENCERRADO!\n')