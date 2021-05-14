from modfuncao import *


def arquivoExiste(nome):
    try:# abrir e rt -> ler arquivo de texto
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:# abrir e wt -> escreve um arquivo de texto '+' cria, caso o arquivo não  exista
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso.')
        
        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possivel abrir o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())
        
 
        
        