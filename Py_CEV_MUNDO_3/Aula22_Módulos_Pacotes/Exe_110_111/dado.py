def leiadinheiro(msg):
    """
    -> Funcao para validar a entrada de dados
    :param msg: recebe os valores digitados e faz as validacoes
    necessarias para evitar erros
    """
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip() # caso seja digitado '.' converte para ',' e se ',' mantem
        if entrada.isalpha(): # se for letras
            print('ERRO! entrada inválida!')
        else:
            # sendo numeros
            valido = True
            return float(entrada)
        
        
def leiataxa(tx):
    """
    -> Funcao para validar a entrada de dados
    :param tx: recebe os valores digitados e faz as validacoes
    necessarias para evitar erros
    """
    valido = False
    while not valido:
        entrada = input(tx).replace(',','.').strip()
        if entrada.isalpha():
            print('ERRO! entrada inválida! ')
        else:
            valido = True
            return float(entrada)
            