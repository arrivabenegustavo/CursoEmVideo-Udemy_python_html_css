''' melhore o exercício 107, formatando os valores para moeda'''

import moedaformat

p = float(input('Digite o preço R$: '))
print(f'A metade de {moedaformat.formatacao(p)} é {moedaformat.formatacao(moedaformat.metade(p))}')
print(f'O dobro de {moedaformat.formatacao(p)} é {moedaformat.formatacao(moedaformat.dobro(p))}')
print(f'Aumentando {moedaformat.formatacao(p)} em 10%, temos {moedaformat.formatacao(moedaformat.aumentar(p, 10))}')
print(f'Diminuindo {moedaformat.formatacao(p)} em 10%, temos {moedaformat.formatacao(moedaformat.diminuir(p, 10))}')