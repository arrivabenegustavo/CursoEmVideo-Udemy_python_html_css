nome = input('Qual seu nome? ')
print('Prazer, {:>20}!'.format(nome))# {alinha para direita}
print('Prazer, {:<20}!'.format(nome))# {alinha para esquerda}
print('Prazer, {:^20}!'.format(nome))# {alinha no centro..total de 20 caracteres}
print('Prazer, {:=^20}!'.format(nome))# {acrescenta um caractere nos espaços}