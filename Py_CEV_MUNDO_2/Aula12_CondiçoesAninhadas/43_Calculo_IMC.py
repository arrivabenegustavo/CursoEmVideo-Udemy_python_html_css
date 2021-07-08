'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida'''
peso = float(input('Digite seu peso(KG): '))
altura = float(input('Digite sua altura(M): '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Seu IMC é {:.1f}\nClassificação: ABAIXO DO PESO.\n\033[1;33mVAI COMER, MAGRELO\033[m'.format(imc))
elif 18<= imc < 25:
    print('Seu IMC é {:.1f}\nClassificação: PESO IDEAL.\n\033[1;32mTA TOOPP!!SHOWW\033[m!!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f}\nClassificação: SOBREPESO.\n\033[1;33mVAI CORRER QUE DA TEMPO!\033[m'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f}\nClassificação: OBESIDADE.\n\033[1;35mCUIDADO\033[m!!!'.format(imc))
else:
    print('Seu IMC é {:.1f}\nClassificação: OBESIDADE MÓRBIDA.\n\033[1;31mDEU RUIM,GORDÃO!!!\033[m'.format(imc))