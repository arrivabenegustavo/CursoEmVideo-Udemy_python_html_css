def aumentar(valor = 0, taxa = 0, formato = False):
    r = (valor * taxa/100) + valor
    return r if not formato else formatacao(r)
    # acrescentado mais um parametro opcional(formato) para dar opção de formatar ou não
    # isso é, se não quiser formatação, deixa false
    # se quiser formatado, acrescente no no código fonte True

def diminuir(valor = 0, taxa = 0, formato = False):
    r = valor - (valor * taxa/100)
    return r if not formato else formatacao(r)


def metade(valor = 0, formato = False):
    r = valor / 2
    return r if not formato else formatacao(r)

    
def dobro(valor = 0, formato = False):
    r = valor * 2
    return r if not formato else formatacao(r)

def formatacao (valor = 0, cifrao = 'R$ '):
    return f'{cifrao}{valor:.2f}'.replace('.', ',')