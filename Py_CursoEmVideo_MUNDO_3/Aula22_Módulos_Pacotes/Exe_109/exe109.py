'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

import moeda2

p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda2.formatacao(p)} é {moeda2.metade(p, True)}')
print(f'O dobro de {moeda2.formatacao(p)} é {moeda2.dobro(p, True)}')
print(f'Aumentando {moeda2.formatacao(p)} em 10%, temos {moeda2.aumentar(p, 10, True)}')
print(f'Diminuindo {moeda2.formatacao(p)} em 10%, temos {moeda2.diminuir(p, 10, True)}')