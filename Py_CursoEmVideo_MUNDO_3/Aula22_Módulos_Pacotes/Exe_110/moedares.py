def aumentar(valor = 0, taxa = 0, formato = False):
    r = (valor * taxa/100) + valor
    return r if not formato else formatacao(r)
  

def diminuir(valor = 0, taxa = 0, formato = False):
    r = valor - (valor * taxa/100)
    return r if not formato else formatacao(r)


def metade(valor = 0, formato = False):
    r = valor / 2
    return r if not formato else formatacao(r)

    
def dobro(valor = 0, formato = False):
    r = valor * 2
    return r if not formato else formatacao(r)

def formatacao(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor = 0, taxaaument = 0, taxadimin = 0):
    print('-' * 30)
    print('RESUMO VALORES'.center(30))
    print('-' * 30)
    print(f'Preço analizado: \t{formatacao(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'{taxaaument}% de aumento: \t{aumentar(valor, taxaaument, True)}')
    print(f'{taxadimin}% de redução: \t{diminuir(valor, taxadimin, True)}')
    print('-' * 30)