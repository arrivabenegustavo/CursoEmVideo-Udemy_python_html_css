import os

caminho_novo = r'C:\users\arriv\onedrive\documentos\gustavo\deucerto'

try:
    os.mkdir(caminho_novo) 
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')
else:
    print('Caminho novo criado com sucesso!')