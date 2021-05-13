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
            print(f'ERRO! {"entrada"} entrada inválida!')
        else:
            # sendo numeros
            valido = True
            return float(entrada)