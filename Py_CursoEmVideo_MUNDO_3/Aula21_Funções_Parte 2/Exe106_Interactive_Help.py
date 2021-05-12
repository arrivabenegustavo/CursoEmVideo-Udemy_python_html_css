''' Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual 
vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''
def ajuda(c):
    help(c)

comando = ' '
while True:
    comando = input('Função ou biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)