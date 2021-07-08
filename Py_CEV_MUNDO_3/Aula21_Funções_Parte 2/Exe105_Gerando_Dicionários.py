'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
e vai retornar um dicionário com as seguintes informações:
- quantidade de notas
- a maior nota
- a menor nota
- media
- situação(opcional)'''

def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situação de varios alunos.
    :param n: uma ou mais notas dos alunos(aceita varias).
    :param sit: (adicional) indicando se quer ou não mostrar a situacao do aluno.
    :return: dicionario com informação das notas e situacao dos alunos.
    """
    valores = dict()
    valores['total'] = len(n)
    valores['maior'] = max(n)
    valores['menor'] = min(n)
    valores['media'] = sum(n) / len(n)
    if sit:
        if valores['media'] >=7:
            valores['situacao'] = 'Boa'
        elif valores[f'media'] >= 5:
            valores['situacao'] = 'Razoável'
        else:
            valores['situacao'] = 'Ruim'
    return valores
print('-'*30)            
valores = notas(5.5, 5.5, 10, 8.5, sit=True)
print(valores)
help(notas)