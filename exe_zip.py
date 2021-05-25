lista_A = [1,2,3,4,5,6,7]
lista_B = [1,2,3,4]

junta_lista = zip(lista_A, lista_B)
soma_lista = [x + y for x, y in junta_lista] 
print(soma_lista) 

#ou

lista_soma = [x + y for x, y in zip(lista_A, lista_B)]
print(soma_lista) 