from typing import final
from interface import *

def ArquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def CriarArquivo(arq):
    try: 
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um erro e arquivo não foi criado.')
    else:
        print(f'Arquivo {arq} criado com sucesso!')
        
def ConteudoArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Arquivo {arq} não pode ser aberto.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()
        
        
def NovoCadastro(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome:<25}{idade:>3} anos\n')
        except:
            print('ERRO! Não foi possível inserir novo cadastro.')
        else:
            print('Dados cadastrados com sucesso!')
            a.close()