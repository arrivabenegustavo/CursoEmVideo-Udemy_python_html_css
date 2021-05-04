# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o número para a oposição {c}: ')))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]           
for posição, elemento in enumerate(valores):
    if elemento == maior:
        print(f'Maior valor foi {maior} na posição {posição}')
    if elemento == menor:
        print(f'Menor valor foi {menor} na posição {posição}')


