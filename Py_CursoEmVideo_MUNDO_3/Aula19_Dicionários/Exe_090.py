''' Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''
alunos = dict()
alunos['nome'] = input('Nome: ')
alunos['media'] = float(input(f'Media de {alunos["nome"]}: '))
if alunos['media'] < 5:
    alunos['situaçao'] = 'Reprovado'
elif alunos['media'] <= 6:
    alunos['situaçao'] = 'Recuperação'
elif alunos['media'] <= 10:
    alunos['situaçao'] = 'Aprovado'
print('-'*30)
for k, v in alunos.items():
    print(f'- {k} é {v}')