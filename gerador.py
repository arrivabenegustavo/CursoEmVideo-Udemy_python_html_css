import sys
#LISTA COMPREHENSION
lista1 = [v for v in range(50)]

#GERADOR -> apenas torcar as chaves para parenteses
lista2 = (v for v in range(50)) 
      
print(sys.getsizeof(lista1))
print(sys.getsizeof(lista2))