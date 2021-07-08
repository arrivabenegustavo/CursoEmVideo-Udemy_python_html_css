# Crie um programa que leia VÁRIOS NÚMEROS vários números inteiros. O programa só vai parar quando digitar 999
# no final, mostra QUANTOS números foram digitados e qual foi a SOMA entre eles, desconsiderando o FLAG 
# FLAG > condição de parada, neste caso é 999

cont = soma = 0
while True:
    n = int(input('Digite um valor ou [999] para parar: '))
    if n == 999:
        break
    cont += 1 # somente para saber quantos números foram digitados
    soma += n # soma o valor dos números digitados
print(f'\nForam digitados {cont} números e a soma foi de {soma}\n')