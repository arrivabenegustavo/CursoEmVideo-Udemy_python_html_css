''' Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso 
de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ESCALENO: todos os lados diferentes
ISÓSCELES: dois lados iguais, um diferente'''
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM FORMAR UM TRIÂNGULO!')
    if r1 == r2 == r3:
        print('Três lados iguais > TRIÂNGULO EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('Todos lados diferentes > TRIÂNGULO ESCALENO.')
    else:
        print('Dois lados iguais e um diferente > TRIÂNGULO ISÓSELES.')
    
else:
    print('As retas NÃO FORMAM UM TRIÂNGULO!')