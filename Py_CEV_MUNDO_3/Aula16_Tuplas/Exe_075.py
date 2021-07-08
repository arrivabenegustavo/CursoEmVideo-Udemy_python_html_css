# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))    
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
números = (n1, n2, n3, n4)
print(f'O número 9 apareceu {números.count(9)} vezes.')
if 3 in números:
    print(f'O número 3 apareceu na {números.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
cont = 0
for n in números:
    if n % 2 == 0:
        cont+= 1
print(f'Foram digitados {cont} valores pares.')
