'''Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
o programa vai perguntar o VALOR DA CASA, o a SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então 
o empréstimo será negado'''

casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Em quantos anos deseja pagar: '))
parcela = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para um empréstimo de R${:.2f} pago em {} anos e'.format(casa,anos, end=''))
print('o valor da parcela será de R${}'.format(parcela))#end='' puxa esse print para linha de cima
if parcela <= minimo:
    print('Parabens!!! Empréstimo \033[1;32mAPROVADO\033[m!')#acréscimo de cor 'APROVADO'
else:
    print('Empréstimo \033[1;31mNEGADO\033[m, seu salário é incompatível com o valor da parcela')#idem
