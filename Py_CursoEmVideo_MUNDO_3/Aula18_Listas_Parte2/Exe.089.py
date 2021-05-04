'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista = []
alunos = []
listamedia = []
media = 0
while True:
    lista.append(input('Nome: '))
    n1 = float(input('Nota1: '))
    lista.append(n1)
    n2 = float(input('Nota2: '))
    lista.append(n2)
    media = (n1 + n2) / 2
    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    opçao= input('Quer continuar?[S/N]: ')
    if opçao in 'Nn':
        break
print()
for pos, aluno in enumerate(alunos):
    print(f'{pos} {aluno[0]}  {aluno[3]}') 
vernota = ' '
while True:
    vernota = int(input('Deseja ver a nota de qual aluno? ([999]finaliza o programa): '))
    if vernota == 1:
        print(f'Notas de {alunos[0][0]} são [{alunos[0][1]}, {alunos[0][2]}]')
    elif vernota == 999:
        break