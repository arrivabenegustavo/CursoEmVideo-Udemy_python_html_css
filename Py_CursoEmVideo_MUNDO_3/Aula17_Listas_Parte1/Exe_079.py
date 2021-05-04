# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
while True:
    n = int(input('Digite um número: '))
    if not n in valores:
        valores.append(n)
        print('Número inserido')
    else:
        print('Número repetido não pode ser inserido!')
        continue
    opção = str(input('Quer continuar: ')).strip().upper()[0]
    if opção in 'N':
        print('Programa finalizado!\n')
        break
valores.sort()
print(f'A lista digitada foi {valores}')