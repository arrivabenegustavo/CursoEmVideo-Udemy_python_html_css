# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

print('-' * 35)
c = 0
while True:
    n = int(input('Digite um número para ver a tabuada: '))
    print('-' * 35)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 15) 
print('\nPROGRAMA TABUADA FINALIZADO, OBRIGADO!\n')
    