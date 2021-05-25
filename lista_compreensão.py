

def espaco(txt):
    print(txt)
    print()


lista = [1,2,3,4,5,6]
lista2 = ['Gustavo','Arrivabene','Thais','Maximo']

exe1 = [v * 2 for v in lista]
exe2 = [v if v % 2 == 0 else 'Impar' for v in lista]


string = '012345678901234567890123456789012345678901234567890123456789'
espaco(f'\nSTRING: {string}')
pulo = 10
contador = [i for i in range(0, len(string), pulo)]
espaco(f'Conta dezenas dentro da STRING: {contador}')
# itera sob inicio e fim de onde será necessário fatiar a L1
inicio_fim = [(i, i +10) for i in range(0, len(string), pulo)]
espaco(f'Mostra inicio e fim de cada dezena : {inicio_fim}')
# faz o fatiamento de L1
retorno_fatido = [string[i:i +10] for i in range(0, len(string),pulo)] 
espaco(f'Mostra STRING fatiada em dezenas {retorno_fatido}')
junta_ponto = '.'.join(retorno_fatido)
espaco(f'Mostra STRING juntada por pontos: {junta_ponto}')