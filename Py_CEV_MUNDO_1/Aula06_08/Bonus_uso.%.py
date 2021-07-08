# Neste exemplo vamos ver o uso do '%' e '.format()' AMBOS TEM A MESMA FUNÇÃO

nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
idade = int(input('Qual sua idade: '))
time = str(input('Qual seu time de coração: '))



#ex com '.format()'
print('O nome é {} e sobrenome é {}'.format(nome, sobrenome))
#ex com '%'
print('%s tem %d e torce para o %s' %(nome, idade, time))
