# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
maior18 = homem = mulher20 = 0
while True:
    print('-'*20)
    print('     CADASTRO     ')
    print('-'*20)
    idade = int(input('Idade: '))    
    sexo = ' '
    while sexo not in 'MF': # Enquanto não digitar M ou F não sairá do laço
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        print('-'*20)
    # a partir daqui, tudo está dentro do primeiro laço
    if idade > 18:
        maior18 += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if sexo == 'M':
        homem += 1
    # Aqui finaliza o programa ou volta para o início.
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\nTotal de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homem} homem(s) cadastrados.')
print(f'E {mulher20} mulhere(s) com menos de 20 anos de idade.')
print('\nCadastros finalizado, obrigado!\n')