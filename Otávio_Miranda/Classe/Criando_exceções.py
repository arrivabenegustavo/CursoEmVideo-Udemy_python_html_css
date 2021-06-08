class EstaErradoError(Exception):
    pass

def testar():
    raise EstaErradoError('Errado')

try:
    testar()
except EstaErradoError as error: # error recebe 'Errado' da linha 5
    print(f'ERRO: {error}')
    