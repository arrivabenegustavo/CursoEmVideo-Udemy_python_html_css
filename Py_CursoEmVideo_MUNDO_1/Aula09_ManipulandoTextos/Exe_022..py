nome = str(input('Digite seu nome: ')).strip() #Método para eliminar os espaços vazios(antes e depois)
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.strip()))) # len + strip pra contar a quantidade de sem espaços
nome_dividido = nome.split() # uma variável para receber uma outra variável com o método aplicado
print('Seu primeiro nome é {} e tem {} letras'.format(nome_dividido[0],len(nome_dividido[0])))