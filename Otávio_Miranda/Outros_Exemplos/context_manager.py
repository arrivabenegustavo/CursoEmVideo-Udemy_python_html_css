'''
Context Manager -> Gerenciador de Contexto

arquivo = open('abc.txt', 'w')
arquivo.write('Testando')
arquivo.close()
'''
# No exemplo acima precisamos abrir e fechar o arquivo, mas as vezes pode acontecer
# de esquecermos de fecharmos o arquivo e ocasionar um erro no programa
# Uma outra opção seria usar um CONTEXT MANAGER:

with open('abc.txt', 'w') as arquivo:
    arquivo.write('testando')

# Porem, é possÍvel tbm criar os próprios geriadores de contexto CONTEXT MANAGER
# caso seja necessário abrir outro tipo de módulo. conexão de rede, base de dados e etc...
# basta fazer a importação e decorar um função

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arq = open (arquivo, modo)
        yield arq
    finally:
        arq.close()

with abrir('abc', 'w') as arquivo:
    arquivo.write('testando 2')

# A função obrigatóriamente precisa ser chamada com o WITH   
