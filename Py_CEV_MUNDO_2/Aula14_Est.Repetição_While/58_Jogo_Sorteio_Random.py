# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar. Mostrado no final quantas 
# tentativas foram necessárias para acertar

from random import randint
computador = randint(0,10)
tentativas = 0
while True:
    tentativas += 1
    jogador = int(input('Escolha um número: '))
    if jogador == computador:
        break
    else:
        if jogador < computador:
            print('Maiss...Tente novamente!')
        else:
            print('Menoss...Tente novamente!')
    
print(f'Acertou!!\nVocê escolheu {jogador} e computador {computador}')
print(f'Precisou de {tentativas} tentativas')
    
    