import pymysql.cursors
from contextlib import contextmanager

# CRUD - CREATE, READ, UPDATE, DELETE

@contextmanager # Gerenciador de contexto
def conecta():
    conexao = pymysql.connect(
        host= '127.0.0.1',
        user= 'root',
        db= 'clientes',
        charset= 'utf8mb4',
        cursorclass= pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print('Conexao fechada')
        conexao.close()
    
# Para qualquer tipo de edição na BASE DE DADOS, é necessário o uso do 
# Gerenciador de contexto WITH

# # INSERE UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        acao = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES'\
#            '(%s, %s, %s, %s)'
#        cursor.execute(acao, ('Gustavo', 'Arrivabene', 31, 98.5))
#        conexao.commit() # necessário para enviar para o banco de dados 


# INSERE VÁRIOS REGISTROS NA BASE DE DADOS        
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         acao = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES'\
#             '(%s, %s, %s, %s)'
#         dados = [
#             ('Thais', 'Maximo', 25, 74),
#             ('KaKaroto', 'Goku', 32, 100),
#             ('Cristiano', 'Ronaldo', 33, 80),
#         ]
# #               executemany para registrar dois dados ou mais
#         cursor.executemany(acao, dados)
#         conexao.commit()


# DELETA UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         acao = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(acao, (16,)) # precisa ser uma tupla, e por ser tupla
#         # com apenas um valor, é necessário a virgula depois do valor
#         conexao.commit()

# DELETA QUANTOS E QUAIS REGISTROS QUISER
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         acao = 'DELETE FROM clientes WHERE id in (%s, %s)'
#         cursor.execute(acao, (18, 20))
#         conexao.commit()
        
# DELETA REGISTROS ENTRE X e Y
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         acao = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(acao, (14, 20))
#         conexao.commit()           

# ATUALIZA/EDITA UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         acao = 'UPDATE clientes SET sobrenome=%s WHERE id=%s'
#         cursor.execute(acao,('Arrivabene', 15))
#         conexao.commit()
    
# SELECIONA OS DADOS DA BASE DE DADOS       
with conecta() as conexao: # Fecha a conexão
    with conexao.cursor() as cursor: # Fecha o cursor
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall()
        
        for linha in resultado:
            print(linha)