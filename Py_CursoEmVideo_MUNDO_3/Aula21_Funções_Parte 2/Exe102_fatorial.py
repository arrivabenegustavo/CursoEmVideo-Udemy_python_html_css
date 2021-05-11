''' Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero.
    :parametro n: numero a ser calculado
    :paramentro show: (opcional) mostrar ou nao o calculo
    :return: O valor fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show: # isto é, se verdadeiro mostra a linha abaixo
            print(f'{c}', end=' ')
            print('x' if c > 1 else '=', end=' ')
        f *= c   
    return f 
    
print(fatorial(5)) # não mostra a conta
print(fatorial(5, show=True)) #mostra a conta
help(fatorial)