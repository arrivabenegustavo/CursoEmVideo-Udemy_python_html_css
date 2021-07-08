#  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados.c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
tabela = ('Flamengo','Inter','AtlMg','Sao Paulo','Fluminense',
          'Gremio','Palmeiras','Santos','AtlPR','Bragantino',
          'Ceara','Corinthians','AtlGO','Bahia','Sport',
          'Fortaleza','Vasco','Goias','Coritiba','Botafogo')
print('\nOs 5 primeiros colocados são:')
print(f'{tabela[:5]}\n')
print('Os 4 últimos são:')
print(f'{tabela[-4:]}\n')
print('Times em ordem alfabética:') 
print(f'{sorted(tabela)}\n')
print('Em que posição está o time São Paulo:')
print(f'O São Paulo está na {tabela.index("Sao Paulo")+1}ª posição')
# Sao Paulo está em aspas duplas por ja existir aspas simples, senão da erro.
# Ou formato abaixo.
#for pos, time in enumerate(tabela):# para analisar a tupla e a posição de cada item dentro dela
#    if time == 'Sao Paulo':
#       print(f'O {time} está na {pos+1}ª posição.\n')


    