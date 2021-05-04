'''Faça um simulador de caixa eletrónico que simule um saque.
notas de 100, 50, 20, 10'''
saque = int(input('Digite o valor que deseja sacar: '))
notas = 100
totalnotas = 0
while True:
    if saque >= notas:
        saque -= notas
        totalnotas += 1
    else:
        if totalnotas > 0:
            print(f'Total de {totalnotas} de R${notas:.2f}')
        elif notas == 100:
            notas = 50
        elif notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        totalnotas = 0
        if saque == 0:
            break
                
    
             
       

    