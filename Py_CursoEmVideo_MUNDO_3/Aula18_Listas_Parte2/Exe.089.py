'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista = []
alunos = []
listamedia = []
media = 0
while True:
    lista.append(input('Nome: '))
    n1 = float(input('Nota1: '))
    n2 = float(input('Nota2: '))
    lista.append([n1,n2]) # para as notas ficarem na mesma lista, isto é na posição 1 da lista principal ALUNOS
    media = (n1 + n2) / 2
    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    opçao= input('Quer continuar?[S/N]: ')
    if opçao in 'Nn':
        break
print(f'{"N°":<4}{"NOME":<8}{"MEDIA":>8}')
for pos, aluno in enumerate(alunos):
    print(f'{pos:<4}{aluno[0]:<10}{aluno[2]:>5}') 
vernota = ' '
while True:
    vernota = int(input('Deseja ver a nota de qual aluno? ([999]finaliza o programa): '))
    if vernota == 999:
        print(f'Finalizado!')
        break
    if vernota < len(alunos):
        print(f'Notas de {alunos[vernota][0]} são {alunos[vernota][1]}')
        