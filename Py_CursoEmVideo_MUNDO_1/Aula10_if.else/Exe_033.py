v1 = int(input('Digite o primero valor: '))
v2 = int(input('Digite o Segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
print(30 *'-')
#Verificando o maior
maior = v1 # igualando um dos valores ao maior, diminui um 'if"..pois independentemente do valor de v1, ele começa sendo considerado como menor
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3  
#Verificando o menor 
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
print('O maior valor foi {}'.format(maior)) 
print('O menor valor foi {}'.format(menor))