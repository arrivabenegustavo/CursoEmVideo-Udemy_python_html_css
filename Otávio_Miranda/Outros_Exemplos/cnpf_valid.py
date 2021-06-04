from validação_cnpj import *
    
cnpj = '11.111.111/1111-11'
cnpj = remove(cnpj)
novo_cnpj = fatia(cnpj)
digito1 = dig1(novo_cnpj)
digito2 = dig2(novo_cnpj + digito1)
validacao = valida(novo_cnpj, digito1, digito2, cnpj)