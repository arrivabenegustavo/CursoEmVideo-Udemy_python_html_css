    
pessoas = [{'nome': 'Gustavo', 'idade': 31},
           {'nome': 'Thais', 'idade': 25},
           {'nome': 'Casamento', 'idade': 1},
           {'nome': 'Namoro', 'idade': 4},
]
# Filter -> Filtra os dados pedido na função
nova_lista = filter(lambda i: i['idade'] > 5, pessoas)
for pessoa in nova_lista:
    print(pessoa)

# list Comprehension -> tbm faz filtro
nova_lista = [i for i in pessoas if i['idade'] > 5]
for pessoa in nova_lista:
    print(pessoa)