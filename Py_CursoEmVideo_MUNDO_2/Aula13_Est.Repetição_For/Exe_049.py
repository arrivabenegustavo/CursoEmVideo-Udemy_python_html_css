#Crie um programa que mostre a tabuada de um número que o usuário escolher
c = 0
while True:
    n = input('Digite um número: ')
    if  not n.isnumeric():
        continue
    else:
        n = int(n)
        break
for c in range (1,11):
    print(f'{n} x {c} = {n*c}')
