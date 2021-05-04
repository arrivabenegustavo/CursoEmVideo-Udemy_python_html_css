'''A Confederação Nacional de Natação precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
 Até 9 anos: MIRIM
 Até 14 anos: INFANTIL
 Até 19 anos: JÚNIOR
 Até 25 anos: SÊNIOR
 Acima de 25 anos: MASTER'''
from datetime import date
anoatual = date.today().year
nome = str(input('Informe o nome do nadador: '))
nasc = int(input('Informe o ano de nascimento: '))
idade = anoatual - nasc
if idade <= 9:
    print('O nadador(a) {} tem {} anos > Categoria: MIRIM.'.format(nome.title(), idade))
elif idade <=14 :
    print('O nadador(a) {} tem {} anos > Categoria: INFANTIL.'.format(nome.title(), idade))
elif idade <= 19:
    print('O nadador(a) {} tem {} anos > Categoria: JUNIOR.'.format(nome.title(), idade))
elif idade <= 25:
    print('O nadador(a) {} tem {} anos > Categoria: SÊNIOR.'.format(nome.title(), idade))
else:
    print('O nadador(a) {} tem {} anos > Categoria: MASTER.'.format(nome.title(), idade))
