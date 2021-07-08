'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
cadastro = {}
cadastro['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
cadastro['Idade'] = date.today().year - nascimento
cadastro['CTPS'] = int(input('Carteira de trabalho ([0] se não tiver): '))
if cadastro['CTPS'] != 0:
    cadastro['contrataçao'] =  int(input('Ano da contratação: '))
    cadastro['Salário'] = float(input('Salário R$: '))
    cadastro['Aposentadoria'] = (cadastro['contrataçao'] + 35) - nascimento
print('-'*30)
for k, v in cadastro.items():
        print(f'- {k} = {v}')
        
    


    


