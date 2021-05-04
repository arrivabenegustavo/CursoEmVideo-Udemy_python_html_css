from random import randint # Função adicional para escolha de um número aleatório
from time import sleep # Função adicional para 'DORMIR'/ESPERAR antes de ir para próxima linha

sorteado = randint(0, 5)#Função add faz o computador "ESCOLHER" um número 
print(55*'-')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ;D')
print(55*'-')
jogador = int(input('Escolha um número: '))#Escolha do usuário
print('PROCESSANDO...')
sleep(2)# Função add (espera por 2 segundos)
if jogador == sorteado:
    print('Acertou miseravi!!')
else:
    print('Deu ruim, pensei no número {}'.format(sorteado))   



