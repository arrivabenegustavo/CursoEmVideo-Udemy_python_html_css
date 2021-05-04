from time import sleep
print(60 * '-')
print('Para viagens acima de 200km haverá um desconto de R$ 0,05/km.')
print(60 * '-')
distancia = float(input('Qual a distância de sua viagem em km: '))
print("CALCULANDO...")
sleep(2)
if distancia <= 200:
    preco = distancia * 0.50
    print('Para {}km o valor será de {:.2f}'.format(distancia, preco))
else:
    preco = distancia * 0.45
    print('Para {}km o valor é de {:.2f}'.format(distancia, preco)) 
    print('\n')   