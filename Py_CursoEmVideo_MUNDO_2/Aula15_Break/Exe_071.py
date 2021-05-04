# Crie um programa que simule o funcionamento de um caixa eletrónico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('\n{:^30}'.format('BANCO 9FIT'))
print('*'*30)
valor = int(input('Quanto(R$) deseja sacar: '))
print('-'*30)
total = valor 
cédula = 50 # Necessário começar com a maior nota
totalcédula = 0 
while True:
# Se o valor digitado for maior que 50, irá subtrair 50 até não conseguir mais
# após todas cédulas de 50 serem tiradas, se necessário, passará para o proximo if
# A cédula mudará de valor sempre que a cédula atual nao puder mais ser subtraída. 
    if total >= cédula: # se o valor do saque for maior que o valor da cédula(que vale 50)
        total -= cédula # subtrai 50 do valor de saque até o valor do saque ser menor que o valor da cédula[50]
        totalcédula += 1 # conta quantas subtrações foram feitas
# Se o valor a ser subtraído for menor que 50, as cédulas vão diminuindo conforme os Ifs abaixo  
# Sempre qu o valor da cédula mudar, será feito o If a cima > valor >= cédula / total -= cédula / totalcédula += 1
    else: 
        if totalcédula > 0: # para mostrar apenas as cédulas que foram necessárias para o saque.
            print(f'Total de {totalcédula} cédulas de R${cédula:.2f}')
        if cédula == 50: # assim que não for mais possível subtrair 50
            cédula = 20 # a Cédula passa a valer 20 e ASSIM SUCESSIVAMENTE até a cédula = 1
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalcédula = 0 # para zerar a total de cédulas sempre que mudar de valor, para fazer a contagem de cada cédula no seu novo valor
        if total == 0: # quando total for igual a 0 acabaram as notas e o programa pode ser encerrado.
            break
print('\nOBRIGADO PELA PREFERÊNCIA!\nTenha um ótimo dia!\n')    