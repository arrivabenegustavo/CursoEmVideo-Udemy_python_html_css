from functools import reduce

produtos = [{'nome':'p1','preco': 25.5},
           {'nome':'p1','preco': 29.9},
           {'nome':'p1','preco': 15},
           {'nome':'p1','preco': 89.9}
 ]

# Reduce -> função para acumular valores, neste caso faz a soma dos preços
soma_preco = reduce(lambda ac, i: ac + i['preco'], produtos, 0)
print(soma_preco)   #ac -> acumula os preços i -> item a serem somados