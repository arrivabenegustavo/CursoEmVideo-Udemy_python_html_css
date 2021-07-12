# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = cont = totprod = 0
barato =' '
print('*'*19)
print('{:^20}'.format('LOJA ARRIVABENE'))# centraliza o texto
print('*'*19)
while True:
    produto = str(input('Nome do Produto: ')).strip().title()
    preço = float(input('Preço R$: '))
    total += preço
    cont += 1 # para contar cada produto
    if preço > 1000:
        totprod += 1
    if cont == 1: # na primeira contagem do laço o MENOR recebe o primeiro PREÇO digitado
        menor = preço
        barato = produto
    else: # após a segunda contagem entra nesse Else. Sempre que o preço for menor trocará o preço guardado no MENOR
        if preço < menor:
            menor = preço
            barato = produto.title() # title para começa a palavra com letra MAIÚSCULA
    #Observe que o bloco if/ else, são iguais > menor = preço / barato = produto
    #Nesse caso é possível simplificar utilizando "OR" > if cont == 1 OR preço < menor > menor = preço / barato = produto
    # com OR uma das 2 declaraçoes precisa ser verdadeira, na primeira passada cont == 1 é verdadeiro, depois somente preço < menor
    continuar = ' '    
    while continuar not in 'SN':
        continuar = str(input('Mais Produtos [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\nO total da compra foi R${total:.2f}')
print(f'Temos {totprod} produtos custando mais que R$ 1000,00')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}\n')
        
    