
from interface import *
from time import sleep 
from arquivo import * 

arq = 'cursoemvideo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resp = menu('Ver pessoas cadastradas','Novo cadastro','Sair do sistema')
    if resp == 1:
        # mostrar conteúdo dentro do arquivo
        ConteudoArquivo(arq)
    elif resp == 2:
        # novos cadastros
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = lerint('Idade: ')
        NovoCadastro(arq, nome, idade)    
    elif resp == 3:
        cabecalho('Sistema finalizado!')
        break
    else:
        print('\033[33mOPÇÃO INEXISTENTE!\033[m')
        sleep(1.5)