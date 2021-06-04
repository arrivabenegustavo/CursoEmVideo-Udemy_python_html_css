'''def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        raise
    
try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)'''
    
# Função RAISE -> Caso aconteça a mesma exceção em qualquer outra parte do códido
# a mensagem de erro já estará logada em ERROR
# neste segundo exemplo criaremos uma mensagem própria de erro para exceção

def divide(n1, n2):
    if n2 == 0:
        raise ValueError('Não existe divisão por 0(zero)') 
    return n1 / n2

try:
    print(divide(2, 0))
except ValueError as error:
    print(error)
    
# Em qualquer outro momento que tivermos o erro ValueError, 
# aparecerá a mensagem criada na linha 19


