from datetime import datetime
from locale import setlocale, LC_ALL 
from calendar import mdays # quantos dias tem cada mês do ano


setlocale(LC_ALL, '') # localiza onde está sendo executado (neste caso BRasil) coloca a data no idioma português
atual = datetime.now()
formatacao = atual.strftime('%A, %B de %B de %Y')
print(formatacao)                                