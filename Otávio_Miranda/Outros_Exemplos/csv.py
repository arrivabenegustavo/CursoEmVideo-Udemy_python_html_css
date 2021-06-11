"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo: # abre para leitura
    dados = [x for x in csv.DictReader(arquivo)] # Através de uma lista comprehension transforma em dicionário
    # isso faz com que possamos usar em um FOR fora do with
    
    #next(dados) # caso tem uma cabeçalho e queira pular
with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )