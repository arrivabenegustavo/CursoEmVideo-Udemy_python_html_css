from random import shuffle # Função adicional para ALEATÓRIAMENTE escolher a ORDEM dos nomes
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto aluno: ')
lista = [n1,n2,n3,n4] # [...]-> representa a lista
shuffle(lista)# função para escolher a ordem dentro da lista
print("A ordem da apresentação será {}".format(lista))
