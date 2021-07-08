# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, 
# mostre uma listagem de preços, organizando os dados em forma tabular.
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
produtos = ('Bola', 55.5, 'Chuteira', 199.9, 'Colete', 10.0, 'Camisa Sao Paulo', 249.9)
for item in range(0, len(produtos)):
    if item % 2 == 0:# item é a posição que está
        print(f'{produtos[item]:.<30}R$',end='')# alinhado a esquerda
    else:
        print(f'{produtos[item]:>7.2f}')# alinhado para direita e 2f par float
print('-' * 40)   

#Explicação
# Como os nomes na lista de produtos estão em posições pares, é possível calcular valores pares
# para mostrar apenas o nomes, portanto, o que nao for par é impar e vai para o fim da linha após end =''