import os

caminho_procura = input(r'Digite um caminho: ')
termo_procura = input('Digite um termo: ')

cont = 0 # para contar a quantidade de arquivos encontrados
# Funcão walk (caminha) percorre sob o caminho desejado
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo: 
            try:  
                caminho_completo = os.path.join(raiz, arquivo) # junta
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo) #separa o nome do arquivo da extensão
                tamanho = os.path.getsize(caminho_completo)
                
                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', extensao_arquivo)
                print('Tamanho:', tamanho)
            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo nãa encontrado.')
            except Exception as e:
                print('Erro desconhecido.', e)
            cont += 1 # contador
print()
print(f'{cont} arquivo(s) encontrado(s).')