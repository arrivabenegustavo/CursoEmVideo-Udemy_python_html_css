import pymysql
from contextlib import contextmanager

from pymysql import cursors


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        db='cadastro',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()


with conecta() as conectado:
    with conectado.cursor() as cursor:
        cursor.execute('SELECT * FROM gafanhotos LIMIT 10')
        listagem = cursor.fetchall()
        for linha in listagem:
            print(linha['id'], linha['nome'])
