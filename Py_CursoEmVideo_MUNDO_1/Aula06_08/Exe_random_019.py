from random import choice # Função adicional para ALEATÓRIAMENTE ESCOLHER' um aluno(str) dentro de uma lista
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Teceiro aluno: ")
n4 = input("Quarto aluno: ")
lista = [n1,n2,n3,n4] # [...] -> representa a lista
sorteado = choice(lista) # uma variável para receber a escolha dentro da lista
print('O aluno escolhido foi {}'.format(sorteado))