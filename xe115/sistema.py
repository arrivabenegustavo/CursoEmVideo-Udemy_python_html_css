
from arquivo import *
from modfuncao import *

arq = 'cursoemvideo.txt' # nome do arquivo
if not arquivoExiste(arq): # se não tem arquivo
    criarArquivo(arq) # cria

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opcao == 1:
        # opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif opcao == 2:
        # opção de cadastrar novas pessoas
        pass
    elif opcao == 3:
        cabecalho('Saindo do programa')    
        break
    else:
         print('\033[31mERRO! Por favor, digite um número válido.\033[m')
    

          