'''Crie um programa que leia duas notas de um aluno e calcule sua média
 mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('O aluno ficou com média de {:.1f} > \033[1;31mREPROVADO!\033[m'.format(media))
elif 5 >= media < 7: # substitui media >=5 and media < 7 > Python aceita esse método para um intervalo entre 2 valores
    print('O aluno ficou com média de {:.1f} > \033[1;33mRECUPERAÇÃO!\033[m'.format(media))
else:
    print('O aluno ficou comm média de {:.1f} > \033[1;32mAPROVADO!\033[m'.format(media))  