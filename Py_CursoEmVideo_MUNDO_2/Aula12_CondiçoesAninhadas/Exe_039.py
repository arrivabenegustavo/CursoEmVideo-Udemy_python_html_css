'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
Se AINDA VAI SE ALISTAR ao serviço  militar / Se é O MOMENTO DE SE ALISTAR ou se JA PASSOU DO TEMPO
Seu programa também deverá mostrar o tempo que falta ou  que passou do prazo, respectivament com as msg.
Se for do sexo feminino não precisa preencher'''


from datetime import date 
ano_atual = date.today().year
print(30*'-')
print('    ALISTAMENTO BRASILEIRO     ')
print(30*'-')
print('''Informe seu sexo:
[1] Masculino
[2] Feminino''')
sexo = int(input('Opção: '))
if sexo == 2 :
    print('Não será necessário o alistamento. OBRIGADO!')
elif sexo == 1: 
    nasc = int(input('Informe o ano de nascimento: '))
    idade = ano_atual - nasc  
    if idade < 18 :
        anos = 18 - idade # quantos anos faltam
        ano_alist = ano_atual + anos # o ano de alistamento
        print('Com {} anos, falta(m) {} anos para se alistar, que será em {}.'.format(idade,anos, ano_alist))
    elif idade == 18:
        print('Com {} anos é o momento de se alistar.\nCORREEEE!!'.format(idade))
    else:
        anos = idade - 18 # quantos anos passaram
        ano_alist = ano_atual - anos # o ano do alistamento
        print('Com {} anos já deveria ter se alistado há {} anos, que seria em {}.'.format(idade,anos,ano_alist))