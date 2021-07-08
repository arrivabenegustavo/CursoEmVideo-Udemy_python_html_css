import dado
import moedares 

p = dado.leiadinheiro('Digite o valor R$: ')
ta = dado.leiataxa('Taxa de aumento: ')
td = dado.leiataxa('Taxa de redução: ')
moedares.resumo(p, ta, td)
help(dado.leiadinheiro)