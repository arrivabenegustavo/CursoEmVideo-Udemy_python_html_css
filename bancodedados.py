import pymysql.cursors
from contextlib import contextmanager

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

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES'\
            '(%s, %s, %s, %s)'
        cursor.execute(sql, ('Gustavo', 'Arrivabene', 31, 98.5))
        conexao.commit() # necessário para enviar para o banco de dados 
    
    
    
    
with conecta() as conexao: # Fecha a conexão
    with conexao.cursor() as cursor: # Fecha o cursor
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall()
        
        for linha in resultado:
            print(linha)