'''Escreva um programa leia DOIS NÚMEROS INTEIROS e compare-os
mostrando na tela uma mensagem: > primeiro valor é maior / segundo valor é maior 
ou não existe valor maior, os dois são iguais'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print('Não existe valor maior, os dois são iguais')