galera = []
dados = []
for c in range(3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear() # exclui o dado pra proxima passagem, senão ele copia o mesmo dado nas outras listas
print(galera)

   
