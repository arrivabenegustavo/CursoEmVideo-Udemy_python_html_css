def aumentar(valor = 0, taxa = 0):
    r = (valor * taxa/100) + valor
    return r


def diminuir(valor = 0, taxa = 0):
    r = valor - (valor * taxa/100)
    return r 


def metade(valor = 0):
    r = valor / 2
    return r 

    
def dobro(valor = 0):
    r = valor * 2
    return r 

def formatacao (valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')