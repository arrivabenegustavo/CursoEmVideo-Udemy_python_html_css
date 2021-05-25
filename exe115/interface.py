def lerint(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[31mENTRADA INVÁLIDA!\033[m Por favor, digite uma opção válida.')
        except KeyboardInterrupt:
            print('\nNão houve entrada!')
            return '"SEM VALOR"'
        else:
            return n 
        
def linha(tam = 42):
    return tam * '-'


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())
    
    
def menu(*lista):
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(lista):
        print(f'{i+1} - {v}')
    print(linha())    
    opcoes = lerint('Opcão: ')
    return opcoes 
