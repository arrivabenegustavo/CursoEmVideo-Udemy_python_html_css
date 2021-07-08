from datetime import date # função add para formato Data
ano = int(input('Qual ano deseja saber?\nDigite 0 se desejar o ano atual: '))
if ano == 0: # caso o usuário digite 0, é chamada a função abaixo. ela trás o ano atual
    ano =  date.today().year # data.hoje().ano -> para mostrar a penas o ano da data atual
if ano % 4==0 and ano % 100 !=0 or ano % 400==0 : 
    print('{} é um ano Bissexto.'.format(ano))
else:
    print('{} NÃO é um ano Bissexto.'.format(ano))

    ''' É divisível por 4 AND Não pode ser divido por 100, pois o resto não é 0 
    OR  e pode ser divido por 400 resto é 0'''
   