carrinho = []

carrinho.append(('Produto',30))
carrinho.append(('Produto 2',20))
carrinho.append(('Produto 3',50))
carrinho.append(('Produto 4', 100))


total = [sum((v[1]) for v in carrinho)]
print(total)