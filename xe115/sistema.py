from arquivo import *
from modfuncao import *

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opcao == 1:
        cabecalho('Opção1')
    elif opcao == 2:
        cabecalho('Opção2')
    elif opcao == 3:
        cabecalho('Saindo do programa')    
        break
    else:
         print('\033[31mERRO! Por favor, digite um número válido.\033[m')
    

          