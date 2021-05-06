'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados 
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas -> LINHA 30
B) A média de idade -> LINHAS (19, 31 e 32)
C) Uma lista com as mulheres -> LINHAS (33 a 36)
D) Uma lista de pessoas com idade acima da média -> LINHAS (37 a 42)'''

cadastros = list()
pessoa = dict()
soma = 0
while True:
    pessoa['nome'] = input('Nome: ').capitalize()
    while True:
        pessoa['sexo'] = (input('Sexo[M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastros.append(pessoa.copy())
    pessoa.clear()
    while True:
        opçao = input('Deseja continuar [S/N]: ').strip().upper()[0]
        if opçao in 'SN':
            break
        print('ERRO! Por favor, digite S ou N.')
    if opçao == 'N':
        break
print(30*'-')
print(f'A) Ao todo foram cadastradas {len(cadastros)} pessoas.')
media = soma / len(cadastros)
print(f'B) A média de idade das pessoas cadastradas foi de {media:.1f} anos.')
print('C) As mulheres cadastradas foram',end=' ')
for p in cadastros:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}',end=' ')
print()   
print('D) A lista com as pessoas a cima da média de idade:')
for p in cadastros: # p (pessoa) = dicionários dentro da lista(cadastros)
    if p['idade'] >= media:
        for k, v in p.items():
            print(f' {k} = {v}',end='; ')
        print()# quebra linha e coloca cada pessoa em uma linha, porem com os dados na mesma linha respectivamente
