'''Escreva um programa  que leia um  número inteiro  qualquer  e peça para o usuário  
escolher qual será  a BASE DE CONVERSAÇÃO  1 para binário - 2 para octal - 3 para hexadecimal'''
# ver video para descobrir como converter os números
print(30 *'-')
print('    CONVERSOR DE BASES     ')
print(30 *'-')
n = int(input("Digite um número inteiro: "))
print('Escolha uma das bases para conversão: ')
print('''[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opçao = int(input("Digite a opção desejada: "))
if opçao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))#fatiamento fora do bin, mas dentro do format
elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))#idem
elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n , hex(n)[2:]))#idem
else:
    print('\033[1;33mOpção inválida!\033[m')
    