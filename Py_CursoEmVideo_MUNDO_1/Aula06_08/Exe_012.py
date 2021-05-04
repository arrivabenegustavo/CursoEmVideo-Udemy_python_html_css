preco = float(input('Digite o preço do produto: '))
novo_preco = preco - (preco * 5 / 100)
print('O preço inicial é de R${:.2f}. \nApós desconto de 5%, o novo valor é R${:.2f}'.format(preco,novo_preco))

# {:.2f}-> dois números decimais, isto é, após a vírgula