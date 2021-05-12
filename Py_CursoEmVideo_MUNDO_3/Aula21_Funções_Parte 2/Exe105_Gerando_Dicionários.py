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
    mai = men = tot = 0
    valores['total'] = len(n)
    for i, v in enumerate(n):
        if i == 0:
            mai = v
            men = v
        else:
            if v > mai:
                mai = v
                valores['maior'] = mai
            if v < men:
                men = v            
                valores['menor'] = men
    valores['media'] = sum(n) / valores['total']
    if sit:
        if valores['media'] <=5:
            valores['situacao'] = 'Ruim'
        elif valores[f'media'] <= 10:
            valores['situacao'] = 'Boa'
    return valores
print('-'*30)            
valores = notas(5.5, 1.5, 10, 8.5)
print(valores)
help(notas)