
def aumenta(idd):
    idd['nova_idade'] = idd['idade'] * 2
    return idd
    
pessoas = [{'nome': 'Gustavo', 'idade': 31},
           {'nome': 'Thais', 'idade': 25},
           {'nome': 'Casamento', 'idade': 1},
           {'nome': 'Namoro', 'idade': 4},
]
   
nova_idade = map(aumenta, pessoas)
for idade in nova_idade:
    print(idade)
    
    
# Exemplo 2
# multiplicar o valores da lista com MAP e LIST COMPREHENSION
lista = [1,2,3,4,5,6]

# O primeiro argumento dentro de MAP necessáriamente deve ser sempre um função, seja qual for
nova_lista = map(lambda n: n * 2, lista)
print(list(nova_lista))
nova_lista2 = [n * 2 for n in lista]
print(nova_lista2)
