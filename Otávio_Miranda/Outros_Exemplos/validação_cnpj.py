import re

def remove(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def fatia(cnpj):
    return cnpj[:12]

def dig1(novo_cnpj):  
    cont = 5
    soma = 0
    for digitos in novo_cnpj:
        soma += cont * int(digitos)
        cont -= 1
        if cont == 1:
            cont = 9
            if cont == 1:
                break  
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    return str(digito)

def dig2(novo_cnpj):  
    cont = 6
    soma = 0
    for digitos in novo_cnpj:
        soma += cont * int(digitos)
        cont -= 1
        if cont == 1:
            cont = 9
            if cont == 1:
                break  
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    return str(digito)

def valida(novo_cnpj, dig1, dig2, cnpj):
    cnpj_completo = novo_cnpj + (dig1 + dig2)
    sequencia = cnpj_completo == cnpj_completo[0] * len(cnpj_completo)
    if cnpj_completo == cnpj and not sequencia:
        print('Cnpj válido')
    else:
        print('Cnpj inválido')
    return cnpj_completo
     
    